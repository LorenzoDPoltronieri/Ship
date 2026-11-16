from scapy.all import ARP, Ether, srp, conf, get_if_addr
import ipaddress
from mac_vendor_lookup import MacLookup, VendorNotFoundError


busca = MacLookup()

def eh_aleatorio(mac: str) -> bool:
    #Diz se o MAC foi inventado pelo aparelho (MAC aleatório).

    return mac[1].upper() in "26AE"


def fabricante(mac: str) -> str:
    #Descobre o fabricante pelo Mec

    if eh_aleatorio(mac):
        return "MAC aleatório"
    try:
        return busca.lookup(mac)
    except VendorNotFoundError:
        return "Desconhecido"


def escanear(rede: str) -> list[dict]:
    #pergunta 'Quem esta ai?' para a rede e devolve quem respondeu.
    pergunta = ARP(pdst=rede)
    envelope = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = envelope / pergunta

    respondidos, _ = srp(pacote, timeout=2, verbose=False)

    dispositivos = []
    for enviado,recebido in respondidos:
        dispositivos.append({
            "ip": recebido.psrc, 
            "mac": recebido.hwsrc,
            "fabricante": fabricante(recebido.hwsrc),
            })
    return dispositivos

def mostrar(dispositivos: list[dict]) -> None:
    #Imprime os dispositivos numa tabela, ordenados por IP.

    ordenados = sorted(dispositivos, key=lambda d: ipaddress.ip_address(d["ip"]))

    print(f"{'IP':<18}{'MAC':<20}{'fabricante'}")
    print("-" * 60)

    for d in ordenados:
        print(f"{d['ip']:<18}{d['mac']:<20}{d['fabricante']}")

    print("-" * 60)
    print(f"Existem {len(ordenados)} Dispositivos nessa rede!") 



def descobrir_rede() -> str:
    #Descobre o ip em que esta logado com a s funções conf.iface e get_if_addr(...)
    meu_ip = get_if_addr(conf.iface)
    rede = ipaddress.ip_network(f"{meu_ip}/24", strict=False)
    return str(rede)



if __name__ == "__main__":
    rede = descobrir_rede()
    print(f"Escaneando a rede {rede}...\n")
    dispositivos = escanear(rede)
    mostrar(dispositivos)