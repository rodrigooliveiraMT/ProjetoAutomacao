export const ELEMENTS = {
    paginaPessoas: {
        btnConsultar: '[id="ctl00_ContentFiltros_btnConsultar"]',
        btnNovo: '[id="ctl00_ContentToolBar_btnNovo"]',
        btnVoltar: '[id="ctl00_ContentToolBar_btnVoltar"]',
        btnSalvar: '[id="ctl00_ContentToolBar_btnSalvaNovo"]',
        btnFinaliza: '[id="ctl00_ContentToolBar_btnSalvar"]',
        inputDescricao: '[id="ctl00_ContentFiltros_txtPesquisa"]',
        dropDowmListpesquisarPor: '[id="ctl00_ContentFiltros_ddlPSQ"]',
        tableResultados: '[id="ctl00_ContentGrid_grdResultados"]',
        colunaTabelaResultadosConsulta: 'tbody tr td:nth-child',
        
    },
    paginaCadastroPessoa:{
        inputNomePessoa: '[id="ctl00_ContentCampos_TabContainer1_tabInformacoes_txtPessoaNome"]',
        inputCPF: '[id="ctl00_ContentCampos_TabContainer1_tabInformacoes_txtPessoaCPF"]',        
        dropDowmListSexo: '[id="ctl00_ContentCampos_TabContainer1_tabInformacoes_ddlPessoaSexo"]',
        inputDataNascimento: '[id="ctl00_ContentCampos_TabContainer1_tabInformacoes_clpPessoaDataNasc"]',
        inputNomeMae: '[id="ctl00_ContentCampos_TabContainer1_tabInformacoes_txtPessoaNomeMae"]',
    }
}