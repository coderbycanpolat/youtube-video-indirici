import requests,time,os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def ytdownloader(yt_url,yt_format):
    try:
        r = requests.get(f'https://loader.to/ajax/download.php?format={yt_format}&url={yt_url}').json()

        stats = r['success']
        title = r['title']
        id = r['id']

        while True:
            get_download = requests.get(f'https://loader.to/ajax/progress.php?id={id}').json()
            download_url = get_download['download_url']

            if 'https' in str(download_url):
                return {'stats': stats, 'title': title, 'download': download_url}

            else:
                print(' - İndiriliyor Bekleyiniz...')
                time.sleep(1.5)
    except:
        return {'stats': False, 'title': 'null', 'download': 'null'}

def home():
    print('\n\n ~~ ̷Y̷̷O̷̷U̷̷T̷̷U̷̷B̷̷E̷ ̷V̷İ̷D̷̷E̷̷O̷ İ̷N̷̷D̷İ̷R̷İ̷C̷İ ~~ \n\n')
    
    print('->> İnstagram : canpolatgkky\n')
    print('->> Telegram : androedit\n')
    print('->> GitHub : coderbycanpolat\n')

   
   
    print('''\n
    - [ 1 ] Başlat
    - [ 2 ] Hangi Formatları Desteklediğine Bakın
    ''')

    stat_input = input(' - Şeçiminiz: ')
    if stat_input == '1':
        cls()
        download_input = input('\n\n - YouTube Video Linkinizi Yapıştırın: ')
        format_input = input(' - Formatı Yazınız [ mp3 , 360 , 720 , 1080 , 4k , 8k ... ]: ')
        data = ytdownloader(download_input, format_input)
        cls()

        if str(data['stats']) != 'true':
            print(' - İndirme Linkiniz [ Tarayıcıya Yapıştırın ]: '+data['download'])
        else:
            print(' - İndirirken Hata Oluştu !')

        print('\n - Geri Dönmek İçin 1 Yazıp Enter Basın')
        input(' - Şeçiminiz: ')
        cls()
        home()

    else:
        cls()
        print('''
    - Tüm Formatlar: 
        mp3
        m4a
        webm_audio
        aac
        flac
        opus
        ogg
        wav
        360
        480
        720
        1080
        4k
        8k
        
    - Geri Dönmek İçin 1 Yazıp Enter Basın
        ''')

    input(' - Seçiminiz: ')
    cls()
    home()

home()