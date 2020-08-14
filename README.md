# ECOP Pocket 2020
## Minicurso de reconhecimento facial usando Python e OpenCV

Este curso é inspirado no projeto desenvolvido por Ashish em sua [Live do Youtube](https://www.youtube.com/watch?v=ukL_UjrqZFw). O projeto foi enriquecido com algumas melhorias de código, a fim de deixar mais legível e automatizar algumas etapas.

### Configurando o ambiente

Utilizaremos um ambiente python comum. Você pode instalar os pacotes necessários direto na raiz, entretanto, utilizar você pode utilziar um ambiente virtual ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) ou [VirtualEnv](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/), sendo o primeiro preferível por mim).
 
Para instalar os pacotes, basta executar `pip install numpy opencv-contrib-python`. Uma vez que os pacotes estejam instalados, basta executar `python run_live_video.py` para verificar se o ambiente está devidamente configurado. Se tudo estiver certo, será aberta uma tela com a imagem da sua webcam, tendo um retângulo destacando a face, com a palavra **Pessoa** sobre ela

**OBS:** para encerrar a execução da webcam, pressione **q** na janela de vídeo. Simplesmente fechá-la irá abrir uma nova tela.