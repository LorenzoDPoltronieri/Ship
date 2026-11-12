from scapy.all import ARP, Ether, srp
import ipaddress

def escanear(rede: str) -> list[dict]:
    #pergunta 'Quem esta ai?' para a rede e devolve quem respondeu.
    pergunta = ARP(pdst=rede)
    envelope = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = envelope / pergunta

    respondidos, _ = srp(pacote, timeout=2, verbose=False)

    dispositivos = []
    for enviado,recebido in respondidos:
        dispositivos.append({"ip": recebido.psrc, "mac": recebido.hwsrc})
    return dispositivos

def mostrar(dispositivos: list[dict]) -> None:
    #Imprime os dispositivos numa tabela, ordenados por IP.

    ordenados = sorted(dispositivos, key=lambda d: ipaddress.ip_address(d["ip"]))

    print(f"{'IP':<18}{'MAC'}")
    print("-" * 35)

    for d in ordenados:
        print(f"{d['ip']:<18}{d['mac']}")

    print("-" * 35)
    print(f"Existem {len(ordenados)} Dispositivos nessa rede!") 



if __name__ == "__main__":
   dispositivos = escanear("192.168.100.0/24")
   mostrar(dispositivos)