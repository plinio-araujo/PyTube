from pytube import YouTube
import os

def main():
    '''
    Inicia as Funções
    '''
    link = input('Insira o link do YouTube')
    chk = input('Precione 1 para VIDEO ou 2 Para Musica')
    if chk == '1':
        print('Baixando Video...')
        x = video(link)        
        (e1,e2) = x
        print(e1)
        print('Erro: ')
        print(e2)
    elif chk == '2':
        print('Baixando a Musica...')
        x = mp3(link)
        (e1,e2) = x
        print(e1)
        print('Erro: ')
        print(e2) 
    else:
        print('Favor Inserir um valor válido')
        
def video(link):
    '''
    Baixa o Arquivo em Video
    '''
    try:        
        caminho = 'c:/users/'+os.getlogin()+'/videos/PyTube/'
        
        yt = YouTube(link)
        stream = yt.streams.get_by_itag(22)
        stream.download(caminho)
        return 'Download Conluido!'
    except Exception as e:
        return 'Falha ao tentar baixar o arquivo!', e
    
def mp3(link):
    '''
    Baixa o arquivo em audio
    '''
    try:
        caminho = 'c:/users/'+os.getlogin()+'/music/PyTube/'        
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        dwn = stream.download(caminho)
        try:            
            muda = yt.title+'mp4'
            arquivo = muda[len(muda)-3:]
            if arquivo != 'mp4':                
                return 'Download Concluido! salvo em MP4'
            else:                
                os.rename(caminho+yt.title+'.mp4', caminho+yt.title + '.mp3')                
                return 'Downlod Concluido! salvo em MP3'
        except Exception as e:
            return 'Download OK\nMas não foi possível renomear o arquivo', e
        
    except Exception as e:
        return 'Falha ao baixar o arquivo! ',e
