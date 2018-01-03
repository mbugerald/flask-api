from app import Application

if __name__ == '__main__':
    Application().import_blue_prints()
    Application().app.run(debug=True)
