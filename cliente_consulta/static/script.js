async function buscaCliente() {
    const doc_cpf = document.getElementById('cpf').value;

    if (!doc_cpf) {
        alert('Por favor, insira um CPF');
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/consulta?doc=${doc_cpf}`);
        const dados = await response.json();

        if (!response.ok) {
            alert(dados.erro || 'Erro na consulta');
            return;
        }

        document.getElementById('nome').textContent = dados.nome;
        document.getElementById('nascimento').textContent = dados.data_nascimento;
        document.getElementById('email').textContent = dados.email;
    } catch (error) {
        alert('Erro ao se conectar com o servidor');
    }
    
    
}

async function cadastrarCliente() {
    const cpf = document.getElementById('cadcpf').value;
    const nome = document.getElementById('cadnome').value;
    const data_nascimento = document.getElementById('cadnascimento').value;
    const email = document.getElementById('cademail').value;

    const payload = {
        cpf,
        dados: { nome, data_nascimento, email }
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/cadastre', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const resultado = await response.json();

        if (!response.ok) {
            alert(resultado.erro || 'Erro ao cadastrar');
        } else {
            alert(resultado.mensagem);
        }
    } catch (error) {
        alert('Erro ao se conectar com o servidor');
    }

    // Força o refresh após o cadastro
    location.reload();
}
