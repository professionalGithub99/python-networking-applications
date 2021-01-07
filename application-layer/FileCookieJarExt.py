from http.cookiejar import FileCookieJar
class FileCookieJarExt(FileCookieJar):
    def save(self,filename):
        print(filename)
