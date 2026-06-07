# GS-SpaceConnect

# 🚀 SpaceConnect - Monitoramento Inteligente de Astronautas

## 👨‍💻 Integrantes

- Andrey Rodrigues Nagata - rm555339
- Henrique Soubhia - rm554493 
- Oliver Kanai Trindade - rm554954 
- Pedro Gutierre Cardoso de Oliveira - rm555445 
- William Weile Feng - rm555132

---

# 🖥️ Ambiente de Desenvolvimento

O projeto foi desenvolvido e testado utilizando:

| Componente | Versão |
|------------|---------|
| Python | 3.12.10 |
| OpenCV | 4.13.0 |
| Sistema Operacional | Windows 11 |
| IDE | Visual Studio Code |

> Observação: Durante o desenvolvimento foram identificadas incompatibilidades entre algumas versões do MediaPipe e o Python 3.13. Por esse motivo, a solução final foi desenvolvida utilizando OpenCV e Python 3.12.

# 📖 Descrição da Solução

Este projeto foi desenvolvido para a Global Solution com o objetivo de aplicar técnicas de Visão Computacional em um contexto relacionado à exploração espacial.

A solução realiza o monitoramento automático da presença de astronautas em áreas críticas de uma base espacial utilizando detecção facial em tempo real.

O sistema captura imagens por meio de uma câmera e utiliza algoritmos de Visão Computacional para identificar rostos humanos, contabilizar astronautas presentes e exibir alertas quando nenhuma pessoa é detectada na área monitorada.

---

# 🎯 Objetivo

Auxiliar no monitoramento de ambientes em bases lunares, estações espaciais ou centros de operação remotos, contribuindo para a segurança e supervisão automatizada dos astronautas.

---

# 🛠️ Bibliotecas Utilizadas

- Python 3
- OpenCV
- NumPy

---

# 🔄 Pipeline de Visão Computacional

```text
Captura de Vídeo
        ↓
Pré-processamento
(Escala de Cinza)
        ↓
Detecção Facial
(Haar Cascade)
        ↓
Contagem de Astronautas
        ↓
Interface e Alertas
```

---

# 📂 Estrutura do Projeto

```text
SpaceConnect-Monitoramento/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SpaceConnect-Monitoramento.git
```

Acesse a pasta do projeto:

```bash
cd SpaceConnect-Monitoramento
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ▶️ Execução

Execute o programa:

```bash
python main.py
```

Para encerrar a aplicação pressione:

```text
ESC
```

---

# 🧠 Funcionamento

O sistema detecta rostos humanos em tempo real e os considera como astronautas presentes na área monitorada.

Quando pelo menos um astronauta é identificado, o sistema exibe:

```text
AREA MONITORADA
```

Caso nenhum astronauta seja detectado:

```text
ALERTA: AREA SEM ASTRONAUTAS
```

Além disso, o sistema:

- Conta a quantidade de astronautas detectados.
- Destaca cada astronauta na tela.
- Atualiza o status da área em tempo real.

---

# 📸 Exemplo de Funcionamento

```text
Astronautas Detectados: 2

STATUS:
AREA MONITORADA
```

ou

```text
Astronautas Detectados: 0

STATUS:
ALERTA: AREA SEM ASTRONAUTAS
```

---

# 💻 Tecnologias Utilizadas

- OpenCV
- Haar Cascade Classifier
- Python
- Visão Computacional

---

# 🌌 Aplicação no Contexto Espacial

Em futuras bases lunares e missões espaciais de longa duração, o monitoramento automatizado da presença de astronautas em áreas críticas pode auxiliar na segurança operacional, no controle de acesso e na supervisão remota dos ambientes.

A solução proposta demonstra como técnicas de Visão Computacional podem ser utilizadas para apoiar atividades relacionadas à economia espacial e à automação de processos.

---

# 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais na disciplina de Visão Computacional.
