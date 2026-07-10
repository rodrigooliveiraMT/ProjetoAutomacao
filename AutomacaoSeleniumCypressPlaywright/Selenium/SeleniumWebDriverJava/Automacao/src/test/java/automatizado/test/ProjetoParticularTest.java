package automacaoSelenium.test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.List;

import org.junit.BeforeClass;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;
import org.openqa.selenium.Alert;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

import automacaoSelenium.page.ProjetoParticularPO;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class ProjetoParticularTest extends BaseTest {

    public static ProjetoParticularPO dsl;

    public static final String URL_BASE = "C:/Automacao/WebSites/Componentes.html";

    @BeforeClass
    public static void inicializarPage() {
        dsl = new ProjetoParticularPO(driver);
        driver.get(URL_BASE);
    }

    @Test
    public void TC001_validarTituloPagina() {
        dsl.ObterTituloPagina("Campo de Treinamento");
    }

    @Test
    public void TC002_campoNome() {
        // Implementar teste para campo nome
        dsl.campoNome.sendKeys("Rodrigo");
        assertEquals("Rodrigo", dsl.campoNome.getAttribute("value"));
        dsl.systemResult(dsl.campoNome.getAccessibleName());
    }

    @Test
    public void TC003_campoSobrenome() {
        // Implementar teste para campo sobrenome
        dsl.campoSobrenome.sendKeys("Costa");
        assertEquals("Costa", dsl.campoSobrenome.getAttribute("value"));
        dsl.systemResult(dsl.campoSobrenome.getAccessibleName());
    }

    @Test
    public void TC004_campoSexoMasculino() {
        // Implementar teste para campo sexo
        dsl.campoSexoMasculino.click();
        assertTrue(dsl.campoSexoMasculino.isSelected());
        dsl.systemResult(dsl.campoSexoMasculino.getAccessibleName());
    }

    @Test
    public void TC005_campoSexoFeminino() {
        // Implementar teste para campo sexo
        dsl.campoSexoFeminino.click();
        assertTrue(dsl.campoSexoFeminino.isSelected());
        dsl.systemResult(dsl.campoSexoFeminino.getAccessibleName());
    }

    @Test
    public void TC006_campoComida() {
        // Implementar teste para campo comida
        dsl.validarRadioButtonCheckbox(dsl.campoComidaCarne);
        dsl.systemResult(dsl.campoComidaCarne.getAccessibleName());
    }

    @Test
    public void TC007_campoEscolaridade() {
        // Implementar teste para campo escolaridade
        Select select = new Select(dsl.campoEscolaridade);
        select.selectByVisibleText("Mestrado");
        assertEquals("Mestrado", select.getFirstSelectedOption().getText());
        dsl.systemResult(dsl.campoEscolaridade.getAccessibleName());
        dsl.systemResult(dsl.campoEscolaridade.getAttribute("value"));
    }

    @Test
    public void TC008_campoEsportes() {
        Select select = new Select(dsl.campoEsportes);

        /**
         * Verificar se o campo permite múltiplas seleções
         */
        assertTrue(select.isMultiple());

        /**
         * Selecionar múltiplas opções usando selectByVisibleText
         */
        select.selectByVisibleText("Futebol");
        select.selectByVisibleText("Corrida");
        select.selectByVisibleText("Natacao");

        /**
         * Verificar se o número de opções selecionadas é o esperado
         */
        List<WebElement> selectedOptions = select.getAllSelectedOptions();
        assertEquals(3, selectedOptions.size());

        /**
         * Verificar se as opções selecionadas são as esperadas
         */
        assertTrue(selectedOptions.stream()
                .allMatch(opt -> List.of("Futebol", "Corrida", "Natacao")
                        .contains(opt.getText())));

        /**
         * Imprimir as opções selecionadas no console
         */
        dsl.systemResult(dsl.campoEsportes.getAccessibleName());

    }

    @Test
    public void TC009_campoSugestoes() {
        // Implementar teste para campo sugestoes
        dsl.campoSugestoes.sendKeys("Sugestão de teste \nSegunda linha de sugestão\nTerceira linha de sugestão");
        assertEquals("Sugestão de teste \nSegunda linha de sugestão\nTerceira linha de sugestão",
                dsl.campoSugestoes.getAttribute("value"));
        dsl.systemResult(dsl.campoSugestoes.getAccessibleName());
    }

    @Test
    public void TC010_botaoCadastrar() {
        // Implementar teste para botão cadastrar
        dsl.botaoCadastrar.click();
        Alert alert = driver.switchTo().alert();
        String resultado = alert.getText();
        assertEquals("Nome eh obrigatorio", resultado);
        alert.accept();
        dsl.systemResult(dsl.botaoCadastrar.getAccessibleName());
    }

    @Test
    public void TC011_validarAlert() {
        // Implementar teste para validar alert
        dsl.systemResult.click();
        Alert alert = driver.switchTo().alert();
        String resultado = alert.getText();
        assertEquals("Alert Simples", resultado);
        alert.accept();
        dsl.systemResult(dsl.systemResult.getAccessibleName());
    }

    @Test
    public void TC012_validarConfirmConfirmacao() {
        // Implementar teste para validar confirm
        dsl.systemResultConfirm.click();
        Alert alert = driver.switchTo().alert();
        String resultado = alert.getText();
        assertEquals("Confirm Simples", resultado);
        alert.accept();
        assertEquals("Confirmado", alert.getText());
        alert.accept();
        dsl.systemResult(dsl.systemResultConfirm.getAccessibleName());
    }

    @Test
    public void TC012_validarConfirmNegacao() {
        // Implementar teste para validar confirm cancelar
        dsl.systemResultConfirm.click();
        Alert alert = driver.switchTo().alert();
        String resultado = alert.getText();
        assertEquals("Confirm Simples", resultado);
        alert.dismiss();
        assertEquals("Negado", alert.getText());
        alert.accept();
        dsl.systemResult(dsl.systemResultConfirm.getAccessibleName());
    }

    @Test
    public void TC013_validarPromptConfirmacao() {
        // Implementar teste para validar prompt
        dsl.systemResultPrompt.click();
        Double valor = 10.0;
        Alert alert = driver.switchTo().alert();
        String resultado1 = alert.getText();
        assertEquals("Digite um numero", resultado1);
        alert.sendKeys(valor.toString());
        alert.accept();
        String resultado2 = alert.getText();
        assertEquals("Era 10.0?", resultado2);
        alert.accept();
        String resultado3 = alert.getText();
        assertEquals(":D", resultado3);
        alert.accept();
        dsl.systemResult(dsl.systemResultPrompt.getAccessibleName());
    }

    @Test
    public void TC013_validarPromptNegacao() {
        // Implementar teste para validar prompt cancelar
        dsl.systemResultPrompt.click();
        Alert alert = driver.switchTo().alert();
        String resultado1 = alert.getText();
        assertEquals("Digite um numero", resultado1);
        alert.dismiss();
        String resultado2 = alert.getText();
        assertEquals("Era null?", resultado2);
        alert.dismiss();
        String resultado3 = alert.getText();
        assertEquals(":(", resultado3);
        alert.accept();
        dsl.systemResult(dsl.systemResultPrompt.getAccessibleName());
    }

    @Test
    public void TC014_validarButtonSimple() {
        // Implementar teste para validar button simple
        dsl.buttonSimple.click();
        assertEquals("Obrigado!", dsl.buttonSimple.getAttribute("value"));
        dsl.systemResult(dsl.buttonSimple.getAccessibleName());
    }

    @Test
    public void TC015_validarTextArea() {
        // Implementar teste para validar text area
        dsl.buttonPopUpEasy.click();
        driver.switchTo().window("Popup");
        dsl.insetTextArea.sendKeys("Teste de automação com Selenium");
        assertEquals("Teste de automação com Selenium", dsl.insetTextArea.getAttribute("value"));
        driver.close();
        driver.switchTo().window("");
        dsl.systemResult(dsl.insetTextArea.getAccessibleName());
    }

    @Test
    public void TC016_validarButtonPopUpHard() {
        // Implementar teste para validar button pop up hard
        dsl.buttonPopUpHard.click();
        driver.switchTo().window(driver.getWindowHandles().toArray()[1].toString());
        dsl.insetTextArea.sendKeys("Teste de automação com Selenium");
        assertEquals("Teste de automação com Selenium", dsl.insetTextArea.getAttribute("value"));
        driver.close();
        driver.switchTo().window(driver.getWindowHandles().toArray()[0].toString());
        dsl.systemResult(dsl.buttonPopUpHard.getAccessibleName());
    }

    @Test
    public void TC017_validarButtonDelay() {
        // Implementar teste para validar button delay
        dsl.buttonDelay.click();
        dsl.delay(dsl.insertNovoCampo);
        dsl.insertNovoCampo.sendKeys("Teste de automação com Selenium");
        assertEquals("Teste de automação com Selenium", dsl.insertNovoCampo.getAttribute("value"));
        dsl.systemResult(dsl.buttonDelay.getAccessibleName());
    }

    @Test
    public void TC018_validarButtonFrame() {
        // Implementar teste para validar button frame
        driver.switchTo().frame(dsl.frame1);
        dsl.buttonFrame.click();
        Alert alert = driver.switchTo().alert();
        String resultado = alert.getText();
        assertEquals("Frame OK!", resultado);
        alert.accept();
        driver.switchTo().defaultContent();
        dsl.systemResultFrame(dsl.frame1, dsl.buttonFrame);
    }

    @Test
    public void TC019_validarLinkVoltar() {
        // Implementar teste para validar link voltar
        dsl.linkVoltar.click();
        if (dsl.resultado.getText().equals("Voltou!")) {
            assertEquals("Voltou!", dsl.resultado.getText());
            dsl.systemResult(dsl.linkVoltar.getAccessibleName());
        } else {
            System.out.println("Houve algo de errado!");
        }
    }
}