import requests
import json
import os
from dotenv import load_dotenv 
from supabase import create_client, Client

load_dotenv()

supabase_url: str = os.getenv("SUPABASE_URL")
supabase_key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

instance_id: str = os.getenv("ZAPI_ID")
api_token: str = os.getenv("ZAPI_TOKEN")

url_zapi = f"https://api.z-api.io/instances/{instance_id}/token/{api_token}/send-text"


def enviar_mensagem():
    try:
        response = supabase.from_('contacts').select('nome, phone').execute()
        contatos = response.data
        
        if not contatos:
            print("Nenhum contato encontrado no Supabase.")
            return

        print(contatos)
        
        for contato in contatos:
            nome = contato.get('nome')
            phone = contato.get('phone')

            if not phone:
                print(f"Atenção: Contato com nome '{nome}' não tem número de telefone. Pulando...")
                continue

            message = f"Olá {nome}, tudo bem com você?"
            
            payload = {
                "phone": phone,
                "message": message
            }

            headers = {
                "Content-type": "application/json",
                "client-token": os.getenv("ZAPI_CLIENT_TOKEN")
            }

            response_zapi = requests.post(url_zapi, data=json.dumps(payload), headers=headers)
            
            print(response_zapi.status_code)

            if response_zapi.status_code == 200:
                print(f"Mensagem enviada com sucesso para {nome} ({phone}).")
            else:
                print(f"Erro ao enviar mensagem para {nome} ({phone}):")
                print(f"Código de status: {response_zapi.status_code}")
                print(f"Resposta: {response_zapi.text}")
            
    except Exception as e:
        print(f"Ocorreu um erro geral: {e}")

if __name__ == "__main__":
    enviar_mensagem()
