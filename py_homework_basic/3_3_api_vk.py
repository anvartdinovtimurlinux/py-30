from pprint import pprint

import requests


TOKEN_VK = '709f6974b00c7b3299e7c5e1be0036e73bac6d72a04732e52b240705704df59b00cff81d7dd15c5510ef1'
API_VERSION_VK = 5.103
URL_VK = 'https://api.vk.com/method/'


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.params = {
            'user_id': self.user_id,
            'access_token': TOKEN_VK,
            'v': API_VERSION_VK,
        }

    def get_friends(self):
        response = requests.get(f'{URL_VK}friends.get', params=self.params)
        return response.json()['response']['items']

    def __and__(self, other):
        friends1 = set(self.get_friends())
        friends2 = set(other.get_friends())
        common_friends = friends1 & friends2
        return list(map(User, common_friends)) or ['Общих друзей не обнаружено']

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'


if __name__ == '__main__':
    print('Программа находит общих друзей у двух пользователей')
    user_id1 = int(input('Введите ID первого пользователя: '))  # 197443101
    user_id2 = int(input('Введите ID второго пользователя: '))  # 1682220

    user1 = User(user_id1)
    user2 = User(user_id2)
    print('\nСписок общих друзей:')
    print(*(user1 & user2), sep="\n")
