from cx_Freeze import setup, Executable



files = ['DataBase.txt', 'new icon.ico','send trans.png','chat logo trans.png']

setup(
    name="Chatbot",
    version="1.0",
    description="Chatbot avec interface de type WhatsApp",
    options={"build_exe": {"include_files": files}},
    executables=[
        Executable(
            "projet.py",
            base="Win32GUI",
            icon="new icon.ico"
        )
    ]
)
