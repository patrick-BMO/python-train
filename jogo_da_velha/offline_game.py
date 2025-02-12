from asciiUi import PublicWordGen
from random import choice

def OfflineGame():
    secret_word, tip = choice(words)
    secret_word = secret_word.lower()
    public_word = PublicWordGen(secret_word)

    return (secret_word, public_word, tip)
                

words = [['Quiroptero', 'morcego'],
['Quitinete', 'pequeno apartamento'],
['Quinquela', 'tipo de barco'],
['Quisquilho', 'coisa insignificante'],
['Quisto', 'tumor'],
['Rabdomante', 'pessoa que procura água com varinha'],
['Rasteira', 'tipo de golpe'],
['Ratel', 'animal parecido com a melgueira'],
['Reaproveitamento', 'uso de materiais descartados'],
['Recanto', 'lugar tranquilo'],
['Reclusa', 'pessoa solitária'],
['Recrudescimento', 'aumento da intensidade'],
['Redoma', 'cobertura de vidro'],
['Refúgio', 'lugar seguro'],
['Regato', 'pequeno rio'],
['Relógio de sol', 'ver o tempo na antiguidade'],
['Remanso', 'lugar calmo em um rio'],
['Renascimento', 'novo nascimento'],
['Reptil', 'animal de sangue frio'],
['Resquícios', 'restos'],
['Retalho', 'pedaço de tecido'],
['Retórica', 'arte de falar bem'],
['Revelação', 'descoberta de algo oculto'],
['Rhapsódia', 'composição musical irregular'],
['Riqueza', 'grande quantidade de bens'],
['Risco', 'perigo'],
['Rituais', 'cerimônias'],
['Robô', 'máquina que imita ações humanas'],
['Roça', 'área cultivada'],
['Roedor', 'animal que rói'],
['Rolha', 'objeto para fechar garrafas'],
['Romã', 'fruta'],
['Ronco', 'som produzido durante o sono'],
['Rosa dos ventos', 'instrumento de orientação'],
['Rosácea', 'doença de pele'],
['Rubi', 'pedra preciosa'],
['Rústico', 'simples, sem refinamento'],
['Sabia', 'ave'],
['Sabugo', 'parte central do milho'],
['Sacerdotisa', 'mulher que serve a um deus'],
['Sagitário', 'sinal do zodíaco'],
['Salmão', 'peixe'],
['Salutar', 'saudável'],
['Salutarismo', 'doutrina que prega a vida saudável'],
['Salvação', 'ato de salvar'],
['Samburá', 'armadilha para peixes'],
['Sanfona', 'instrumento musical'],
['Sanguessuga', 'animal que suga sangue'],
['Santuário', 'lugar sagrado'],
['Sapinho', 'pequeno anfíbio'],
['Sarcófago', 'caixão de pedra'],
['Sardinha', 'peixe'],
['Satelite', 'corpo celeste que gira em torno de um planeta'],
['Saturado', 'encharcado'],
['Saudade', 'sentimento de falta'],
['Saxofone', 'instrumento musical'],
['Sebo', 'loja de livros usados'],
['Seca', 'falta de chuva'],
['Sedentarismo', 'falta de atividade física'],
['Seiva', 'líquido que circula nas plantas'],
['Selênio', 'elemento químico'],
['Semente', 'origem de uma planta'],
['Serpente', 'réptil'],
['Serpentear', 'mover-se em curvas'],
['Sertão', 'região seca'],
['Sesmaria', 'grande extensão de terra'],
['Símio', 'macaco'],
['Simpósio', 'reunião para discutir um tema'],
['Sinônimo', 'palavra com significado semelhante'],
['Sirene', 'som alto para alertar'],
['Sisal', 'fibra vegetal'],
['Sismógrafo', 'aparelho para medir terremotos'],
['Sótão', 'compartimento sob o telhado'],
['Sovaco', 'parte do corpo'],
['Suricate', 'animal mamífero'],
['Suspiro', 'ato de respirar fundo'],
['Tacacá', 'prato típico da Amazônia'],
['Tapete voador', 'objeto mágico'],
['Tarântula', 'aranha grande e peluda'],
['Tartaruga', 'réptil de casco'],
['Tasca', 'pequeno bar'],
['Tebas', 'cidade antiga'],
['Telhado', 'cobertura de um edifício'],
['Tempo', 'duração'],
['Tenaz', 'forte'],
['Tendão', 'parte do corpo'],
['Terraplanismo', 'teoria que a Terra é plana'],
['Tesouro', 'riqueza escondida'],
['Timbre', 'qualidade do som'],
['Timbó', 'planta usada para pescar'],
['Titã', 'gigante da mitologia grega'],
['Toca', 'abrigo de animais'],
['Tolda', 'cobertura para proteger do sol'],
['Torpor', 'estado de letargia'],
['Torrão', 'pedaço de terra seca'],
['Trapiche', 'pequeno cais'],
['Tribo', 'grupo social'],
['Trombeta', 'instrumento musical'],
['Tufão', 'vento forte']]