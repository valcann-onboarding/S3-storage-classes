# Mudança do S3 storage classes em milhões objetos 

Proposta para agilizar o restore e copy com mudança de storage class em objetos em um Bucket S3. 

## Descrição

Na execução do script para fazer o restore de 100.000 objetos utilizando uma única "máquina", foi observada a seguinte estimava:
```
2022-05-09 19:26:39,341 - INFO - restore> XXXX_XXXX_XXXX_XXXX_XXXX_.jpg
2022-05-09 19:26:41,100 - INFO - restore> XXXX_XXXX_XXXX_XXXX_XXXX_.jpg
2022-05-09 19:26:47,964 - INFO - restore> XXXX_XXXX_XXXX_XXXX_XXXX_.jpg
...
2022-05-09 22:18:21,100 - INFO - restore> XXXX_XXXX_XXXX_XXXX_XXXX_.jpg
2022-05-09 22:18:22,925 - INFO - restore> XXXX_XXXX_XXXX_XXXX_XXXX_.jpg
2022-05-09 22:18:24,872 - INFO - restore> XXXX_XXXX_XXXX_XXXX_XXXX_.jpg
---
~aprox 5mil objetos em 3h, isso implica em aproximadamente 2 dias e meio para concluir o restore de 100mil objetos.
```
Também, foi descoberto que a velocidade para fazer o restore dos objetos é limitada pela velocidade de execução do comando pela awscli.
Então, a ideia foi subdividir 100mil objetos em 20 lots menores, onde cada lote menor ia ser processados em containers.

## Pré-requisitos

1. Ter um arquivo com os nomes desses objetos no bucket
2. Certificar-se de estar com o python, docker e awscli instalados

## Começando

### Dependências

* WSL no Windows

### Hands-on

```bash
# Primeira Parte

# Criação dos lots menores
split -l 5000 -d -a 2 arquivo.txt

# Criação das folders para representar o cluster ECS
mkdir NOME_DA_PASTA

# Dentro da folder é preciso ter:
# 1. Dockerfile
# 2. lots menores
# 3. restore_objects.py
# 4. change_object_storage_class_with_copy.py
# 5. run_fargate.py

# Veja a pasta `exemplo` para detalhes
```


```bash
# Segunda Parte

# Abra no AWS Console o ECS, ECR e S3
# Crie um repo no ECR e siga as instruções de push
# Crie um Cluster no ECS para fargate
# No ECS entre em Task Definition e crie duas tasks
# Crie uma task para o restore
# Crie uma task para o copy with change storage class
# (Opcional) Verifique o arquivo run_fargate.py
# E então:

python run_fargate.py
```

## Autores

Gabriel Nogueira  
[@gabrielnogueira12](https://www.linkedin.com/in/gabrielnogueira12/)

Matheus Silva  
[@silvamva](https://twitter.com/silvamva)

## Histórico de versões

* 0.1
    * Solução inicial

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE.md para detalhes.

## Referências

Inspiração, trechos de código, etc.
* [pywren](http://pywren.io/)
* [ecs-boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html)
