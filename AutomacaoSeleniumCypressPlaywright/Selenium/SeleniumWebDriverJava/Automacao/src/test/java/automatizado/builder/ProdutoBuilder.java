package automatizado.builder;

import automatizado.page.ControleDeProdutoPO;

public class ProdutoBuilder {
    
    public Integer codigo = 0001;
    public String nome = "Produto Teste";
    public Integer quantidade = 1;
    public Double valor = 1.0;
    public String data = "08/04/2025";

    protected ControleDeProdutoPO controleProdutoPage;

    public ProdutoBuilder(ControleDeProdutoPO controleDeProdutoPO){
        this.controleProdutoPage = controleDeProdutoPO;
    }

    public ProdutoBuilder adicionarCodigo(Integer codigo){
        this.codigo = codigo;
        return this;
    }

    public ProdutoBuilder adicionarNome(String nome){
        this.nome = nome;
        return this;
    }

    public ProdutoBuilder adicionarQuantidade(Integer quantidade){
        this.quantidade = quantidade;
        return this;
    }

    public ProdutoBuilder adicionarValor(Double valor){
        this.valor = valor;
        return this;
    }

    public ProdutoBuilder adicionarData(String data){
        this.data = data;
        return this;
    }

    public void builder(){
        controleProdutoPage.escrever(controleProdutoPage.inputCodigo, (codigo != null) ? codigo.toString() : "");
        controleProdutoPage.escrever(controleProdutoPage.inputNome, nome);
        controleProdutoPage.escrever(controleProdutoPage.inputQuantidade, (quantidade != null) ? quantidade.toString() : "");
        controleProdutoPage.escrever(controleProdutoPage.inputValor, (valor != null) ? valor.toString() : "");
        controleProdutoPage.escrever(controleProdutoPage.inputData, data);

        controleProdutoPage.buttonSalvar.click();
    }
}
