def siteOn(url):
    import urllib
    import urllib.request
    from uteis.cores import cores
    try:
        site = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print(f'{cores.text["red"]}O site não está acessível no momento.{cores.style["none"]}')
    else:
        print(f'{cores.text["purple"]}O site está acessível no momento.{cores.style["none"]}')
        #print(site.read())
    finally:
        print(f'{cores.text["green"]}Fim da execução.{cores.style["none"]}')

siteOn('http://www.pudim.com.br')