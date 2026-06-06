''''
SITUACAO HIPOTÉTICA -

Fomos contratados para coordenar o setor de data science da DataSciencester, a rede social dos cientistas de dados.

O vice presidente quer que você identifique os "conectores-chaves" entre os cientistas de daddos.
Para isso ele disponibiliza um data dump da rede DataSciencester.

Esse dump trata-se de uma lista em que cada usuário é representado por um dict(dicionário), que contém id e nome.
Você também recebe os dados de "amizades", reunidos em  uma lista de pares de IDs.

'''

#dados de usuários
users = [
{"id": 0, "name": "Hero"},
{"id": 1, "name": "Dunn"},
{"id": 2, "name": "Sue"},
{"id": 3, "name": "Chi"},
{"id": 4, "name": "Thor"},
{"id": 5, "name": "Clive"},
{"id": 6, "name": "Hicks"},
{"id": 7, "name": "Devin"},
{"id": 8, "name": "Kate"},
{"id": 9, "name": "Klein"},
]

#dados de amizades
friendship_pairs = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

'''
Representar as amizades em uma lista de pares não é muito eficiente. Para encontrar todas as amizades  do usuário 1, você precisa iterar todos os
pares em busca dos que contêm 1. Se houver um grande números de pares, isso levará muito tempo.

Em vez disso criaremos um dict onde as chaves serão os ids dos usuários e os valores serão listas com os ids dos seus amigos(É muito rápido pesquisar em um dict).
'''

#Inicializa um dict com um lista vazia para cada usuário
friendships = {user["id"]: [] for user in users}

#print(friendships)

#Em seguida, executa um loop pelos pares de amigos para preechê-la
for usuario, amigo in friendship_pairs:
    friendships[usuario].append(amigo) #grava a relacao tanto em um usuário como no outro.
    friendships[amigo].append(usuario)

#print(friendships)



'''
Agora que colocamos as amizades em um dict, podemos facilmente fazer perguntas ao nosso grafo, como:'Qual é o número  médio de conexões?'
'''

def number_of_friends(user):
    #quantos amigos tem o user?
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

#soma o total de amigos de cada id de usuario
total_connections = sum(number_of_friends(user) for user in users)

#print(total_connections)

num_users = len(users)

#tirando a média das conexoes
avg_connections = total_connections/num_users


'''
Podemos também encontrar as pessoas mais conectadas - as que possuem o maior número de amigos.
'''

total_connections_user = [(user["id"],number_of_friends(user)) for user in users]

total_connections_user.sort(key = lambda ordernarPeloValor: ordernarPeloValor[1], reverse=True) #usa o comando lambda para ordenar pelo valor e traz o resultado do maior pro menor

#print(total_connections_user)



'''
Agora precisam que você desenvolva um sugestor do tipo "Cientistas de dados que você talvez conheça"
'''

def foaf_ids_bad(user): #foaf = friend od a friend
    return [foaf_id
                for friend_id in friendships[user["id"]]
                for foaf_id in friendships[friend_id]
    ]


for user in users:
    print(f"Amigos do id {user["id"]} : {foaf_ids_bad(user)}") #Esse resultado gera os valores com redundancia.
    


'''
Vamos gerar uma contagem de amigos em comum, porém excluindo as pessoas que o usuário já conhece
'''

from  collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

print(friends_of_friends(users[3]))
