\## Como abrir o projeto

cd $HOME\\SHIP

.\\.venv\\Scripts\\Activate.ps1

git status



\\\\IP da casa



192.168.100.0/24



É isso que o scanner vai usar na Fase 2.



192.168.100.1         e0-4b-a6-9a-a9-ca     dinâmico  / ROTEADOR

192.168.100.87        f6-22-b0-dc-98-40     dinâmico  / Meu telefone

192.168.100.44        a8-16-9d-d1-2a-76     dinâmico  / ?????

192.168.100.9         dc-4e-f4-0a-e6-03     dinâmico  / ?????







O arp -a só mostra aparelhos com quem o PC já conversou. Por isso o SHIP vai gritar pra rua inteira em vez de olhar a agenda: assim ele acha todo mundo, até quem nunca falou com o PC.



\##Subir o Diário

git add DIARIO.md

git commit -m "Diario: Fase 1, mapeamento manual da rede"

git push





Com o time out 10 apareceu mais 2 ips



Aparelhos em modo economia de energia podem não responder ao scan, realizado o teste com o próprio telefone.





\###############################################################################



A ordenação dos Ips em Python não é funcional porque a mesma olha caractere por caractere, assim em um exempor o 25 vira antes do numero 3 em uma ordem. 





