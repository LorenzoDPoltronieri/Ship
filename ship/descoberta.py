from scapy.all import ARP, Ether, srp
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



if __name__ == "__main__":
   dispositivos = escanear("192.168.100.0/24")
   mostrar(dispositivos)