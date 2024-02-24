from livereload import Server, shell


def main():
    server = Server()
    server.watch('index.html', shell('make html'))
    server.serve(root='.')


if __name__ == '__main__':
    main()
