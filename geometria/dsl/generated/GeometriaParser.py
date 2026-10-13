# Generated from outputs/geometria/dsl/Geometria.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,36,8,2,10,2,12,2,39,9,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,3,5,
        57,8,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,10,11,58,0,15,1,0,
        0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,43,1,0,0,0,8,49,1,0,0,0,10,56,1,
        0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,
        16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,
        0,20,23,3,4,2,0,21,23,3,6,3,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,
        0,0,0,24,25,5,1,0,0,25,26,5,13,0,0,26,27,5,2,0,0,27,28,5,3,0,0,28,
        29,3,8,4,0,29,30,5,4,0,0,30,31,3,8,4,0,31,32,5,4,0,0,32,37,3,8,4,
        0,33,34,5,4,0,0,34,36,3,8,4,0,35,33,1,0,0,0,36,39,1,0,0,0,37,35,
        1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,5,0,0,
        41,42,5,6,0,0,42,5,1,0,0,0,43,44,5,7,0,0,44,45,5,8,0,0,45,46,5,13,
        0,0,46,47,5,9,0,0,47,48,5,6,0,0,48,7,1,0,0,0,49,50,5,8,0,0,50,51,
        3,10,5,0,51,52,5,4,0,0,52,53,3,10,5,0,53,54,5,9,0,0,54,9,1,0,0,0,
        55,57,7,0,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,
        12,0,0,59,11,1,0,0,0,4,15,22,37,56
    ]

class GeometriaParser ( Parser ):

    grammarFileName = "Geometria.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'poligono'", "'='", "'['", "','", "']'", 
                     "';'", "'area'", "'('", "')'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "ID", "COMENTARIO", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_declaracion = 2
    RULE_consulta = 3
    RULE_punto = 4
    RULE_numero = 5

    ruleNames =  [ "programa", "sentencia", "declaracion", "consulta", "punto", 
                   "numero" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NUM=12
    ID=13
    COMENTARIO=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GeometriaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeometriaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(GeometriaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return GeometriaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = GeometriaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==7:
                self.state = 12
                self.sentencia()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(GeometriaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(GeometriaParser.DeclaracionContext,0)


        def consulta(self):
            return self.getTypedRuleContext(GeometriaParser.ConsultaContext,0)


        def getRuleIndex(self):
            return GeometriaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = GeometriaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.declaracion()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.consulta()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GeometriaParser.ID, 0)

        def punto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeometriaParser.PuntoContext)
            else:
                return self.getTypedRuleContext(GeometriaParser.PuntoContext,i)


        def getRuleIndex(self):
            return GeometriaParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = GeometriaParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(GeometriaParser.T__0)
            self.state = 25
            self.match(GeometriaParser.ID)
            self.state = 26
            self.match(GeometriaParser.T__1)
            self.state = 27
            self.match(GeometriaParser.T__2)
            self.state = 28
            self.punto()
            self.state = 29
            self.match(GeometriaParser.T__3)
            self.state = 30
            self.punto()
            self.state = 31
            self.match(GeometriaParser.T__3)
            self.state = 32
            self.punto()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 33
                self.match(GeometriaParser.T__3)
                self.state = 34
                self.punto()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(GeometriaParser.T__4)
            self.state = 41
            self.match(GeometriaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsultaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GeometriaParser.ID, 0)

        def getRuleIndex(self):
            return GeometriaParser.RULE_consulta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsulta" ):
                listener.enterConsulta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsulta" ):
                listener.exitConsulta(self)




    def consulta(self):

        localctx = GeometriaParser.ConsultaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_consulta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(GeometriaParser.T__6)
            self.state = 44
            self.match(GeometriaParser.T__7)
            self.state = 45
            self.match(GeometriaParser.ID)
            self.state = 46
            self.match(GeometriaParser.T__8)
            self.state = 47
            self.match(GeometriaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PuntoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numero(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GeometriaParser.NumeroContext)
            else:
                return self.getTypedRuleContext(GeometriaParser.NumeroContext,i)


        def getRuleIndex(self):
            return GeometriaParser.RULE_punto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPunto" ):
                listener.enterPunto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPunto" ):
                listener.exitPunto(self)




    def punto(self):

        localctx = GeometriaParser.PuntoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_punto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(GeometriaParser.T__7)
            self.state = 50
            self.numero()
            self.state = 51
            self.match(GeometriaParser.T__3)
            self.state = 52
            self.numero()
            self.state = 53
            self.match(GeometriaParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(GeometriaParser.NUM, 0)

        def getRuleIndex(self):
            return GeometriaParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)




    def numero(self):

        localctx = GeometriaParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==11:
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 58
            self.match(GeometriaParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





