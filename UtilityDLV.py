from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from languages.asp.asp_input_program import ASPInputProgram
from base.option_descriptor import OptionDescriptor

class UtilityDLV:

    def __init__(self):
        self.fatti = ""
        self.regole = ""
        #self.handler = DesktopHandler(DLV2DesktopService("C:/Users/Micha/Desktop/IA/Progetto/lib/dlv2.exe"))
        self.handler = DesktopHandler(DLV2DesktopService("../dlv2.exe"))

        self.program = ASPInputProgram()

    def getSoluzione(self):
        answersets = self.handler.start_sync()

        for a in answersets.get_answer_sets():
            print(str(a))
            #return int(self.getColonna(str(a)))

    def getColonna(self, scelta):
        return scelta[11]

    def trasferisciInDLV(self):
        self.program.add_program(self.fatti)
        self.program.add_files_path("regole.txt")
        
        self.handler.add_program(self.program)

    def setFatti(self, matrice, blocco):
        self.fatti = matrice
        self.fatti +=  "b(" + str(blocco) + ")."

   




