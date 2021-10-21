import report_gen
import main


def compileAll():
    def compileReport():
        report_gen.runner()

    def compileMain():
        main.runner()

    compileReport()
    compileMain()


compileAll()
