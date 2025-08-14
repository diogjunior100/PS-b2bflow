# PS-b2bflow

## Setup

1. Configure uma tabela no Supabase:
   - Acesse o [Supabase](https://supabase.com/).
   - Crie um novo projeto ou use um existente.
   - Configure a tabela necessária para o projeto com as colunas apropriadas.

2. Obtenha as chaves de API do Supabase:
   - Vá para a aba "Settings" do seu projeto no Supabase.
   - Copie as chaves `SUPABASE_URL` e `SUPABASE_KEY`.

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```
SUPABASE_URL=<sua_url_supabase>
SUPABASE_KEY=<sua_chave_supabase>
ZAPI_KEY=<sua_chave_zapi>
```

Substitua `<sua_url_supabase>`, `<sua_chave_supabase>` e `<sua_chave_zapi>` pelos valores apropriados.

## Como Rodar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o projeto:
   ```bash
   python main.py
   ```