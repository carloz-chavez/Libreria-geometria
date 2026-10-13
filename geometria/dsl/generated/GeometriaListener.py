# Generated from outputs/geometria/dsl/Geometria.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GeometriaParser import GeometriaParser
else:
    from GeometriaParser import GeometriaParser

# This class defines a complete listener for a parse tree produced by GeometriaParser.
class GeometriaListener(ParseTreeListener):

    # Enter a parse tree produced by GeometriaParser#programa.
    def enterPrograma(self, ctx:GeometriaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by GeometriaParser#programa.
    def exitPrograma(self, ctx:GeometriaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by GeometriaParser#sentencia.
    def enterSentencia(self, ctx:GeometriaParser.SentenciaContext):
        pass

    # Exit a parse tree produced by GeometriaParser#sentencia.
    def exitSentencia(self, ctx:GeometriaParser.SentenciaContext):
        pass


    # Enter a parse tree produced by GeometriaParser#declaracion.
    def enterDeclaracion(self, ctx:GeometriaParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by GeometriaParser#declaracion.
    def exitDeclaracion(self, ctx:GeometriaParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by GeometriaParser#consulta.
    def enterConsulta(self, ctx:GeometriaParser.ConsultaContext):
        pass

    # Exit a parse tree produced by GeometriaParser#consulta.
    def exitConsulta(self, ctx:GeometriaParser.ConsultaContext):
        pass


    # Enter a parse tree produced by GeometriaParser#punto.
    def enterPunto(self, ctx:GeometriaParser.PuntoContext):
        pass

    # Exit a parse tree produced by GeometriaParser#punto.
    def exitPunto(self, ctx:GeometriaParser.PuntoContext):
        pass


    # Enter a parse tree produced by GeometriaParser#numero.
    def enterNumero(self, ctx:GeometriaParser.NumeroContext):
        pass

    # Exit a parse tree produced by GeometriaParser#numero.
    def exitNumero(self, ctx:GeometriaParser.NumeroContext):
        pass



del GeometriaParser