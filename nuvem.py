import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 🔓 Destrava a segurança de rede
from pydantic import BaseModel
import edge_tts
from datetime import datetime
import random

# Inicializa o servidor web da Kira
app = FastAPI(title="K.I.R.A. AI - Nuvem Core")

# Configuração do Middleware de CORS para aceitar mensagens de qualquer app/celular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite conexões de qualquer lugar do mundo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComandoUsuario(BaseModel):
    texto: str
    usuario: str = "Senhor"

def obtener_saudacao_temporal():
    hora_atual = datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

@app.get("/")
def status_servidor():
    return {"status": "online", "sistema": "K.I.R.A. AI Core", "nuvem": "ativa"}

@app.post("/perguntar")
def processar_mente_nuvem(dados: ComandoUsuario):
    texto = dados.texto.lower().strip()
    texto_limpo = texto.replace("kira", "").replace("sara", "").replace("jarvis", "").replace("oi", "").replace("abra", "").replace("abre", "").strip()
    
    saudacao = obtener_saudacao_temporal()
    nome = dados.usuario
    
    if "horas" in texto_limpo or "hora" in texto_limpo:
        hora_formatada = datetime.now().strftime('%H horas e %M minutos')
        resposta = f"Sincronização de nuvem concluída. Agora são exatamente {hora_formatada}, {nome}."
        
    elif "data" in texto_limpo or "dia" in texto_limpo:
        data_formatada = datetime.now().strftime('%d de %B')
        resposta = f"Calendário orbital checado. Hoje é dia {data_formatada}, {nome}."
        
    elif "piada" in texto_limpo or "conte algo engraçado" in texto_limpo:
        lista_piadas = [
            "Por que o computador foi ao médico? Porque ele estava com um vírus de sistema.",
            "O que o código Python disse para o café? Sem você, eu não compilo de manhã.",
            "Existem 10 tipos de pessoas no mundo: as que entendem binário e as que não entendem."
        ]
        resposta = f"Acessando banco de dados humorísticos na nuvem. {random.choice(lista_piadas)}"

    elif any(palavra in texto_limpo for palavra in ["boa noite", "bom dia", "boa tarde"]):
        resposta = f"{saudacao}, {nome}. Servidores em nuvem online. Como posso ser útil nas suas tarefas remota?"

    elif any(palavra in texto_limpo for palavra in ["tudo bem", "como vai", "status"]):
        resposta = f"{saudacao}, {nome}. Todos os meus núcleos em nuvem estão operando com estabilidade e lógica em 100%."
        
    elif any(palavra in texto_limpo for palavra in ["oi", "olá", "acordada"]):
        resposta = f"Sistemas de prontidão em segundo plano na nuvem. {saudacao}, {nome}. Eu sou a Kira."
        
    else:
        resposta = f"Frequência de nuvem recebida, {nome}, mas o comando enviado ainda não possui braços de automação web."

    return {
        "comando_recebido": dados.texto,
        "resposta_kira": resposta,
        "perfil": nome
    }
