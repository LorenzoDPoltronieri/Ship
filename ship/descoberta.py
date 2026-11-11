from scapy.all import ARP, Ether, srp

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

if __name__ == "__main__":
    for d in escanear("192.168.100.0/24"):
        print(d)