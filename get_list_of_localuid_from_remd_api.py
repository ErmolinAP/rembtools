import requests


def get_list_of_localuid_from_remd_api(list_size=20, c_page=0, s_Date='2023-01-01', e_Date='2023-02-23'):
    uids = []

    def get_list_Uid(host='127.0.0.1',
                     port='18083',
                     pageSize=20,
                     pageNumber=0,
                     semd_kind='{\"code\": \"75\"}',
                     cDateBegin='2023-02-22',
                     cDateEnd='2023-02-23',
                     endpoint='/emds/reg/rest/api/v1/documents/'):

        url = "http://{}:{}{}?pageSize={}&pageNumber={}&kind={}&creationDateBegin={}&creationDateEnd={}".format(
            host, port, endpoint, pageSize, pageNumber, semd_kind, cDateBegin, cDateEnd)

        list_uid = []
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        response_data = response.json()

        content = response_data['content']

        for record in content:
            list_uid.append(record['localUid'])

        return list_uid, response_data['last'], url

    while True:

        fetched_list = get_list_Uid(pageSize=list_size, pageNumber=c_page, cDateBegin=s_Date, cDateEnd=e_Date)

        if fetched_list[1]:
            print('Страница', c_page, '- последняя страница, получено', len(fetched_list[0]), 'записей')
            uids.extend(fetched_list[0])
            break
        else:
            print('Страница', c_page, ', получено', len(fetched_list[0]), 'записей')
            uids.extend(fetched_list[0])
            c_page += 1

    return len(uids), uids
