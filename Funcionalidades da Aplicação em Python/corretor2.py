import language_tool_python

# Criação de objeto 
tool = language_tool_python.LanguageToolPublicAPI('pt-BR')

# Entrada do usuário
entrada = input('Digite algo para ser corrigido: ')

# Verificação e correção da entrada do usuário
correcao = tool.correct(entrada)

# Imprimir
print('Entrada corrigida:', correcao)