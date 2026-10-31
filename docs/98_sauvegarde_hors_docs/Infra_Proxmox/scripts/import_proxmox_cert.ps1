# Import certificat CA Proxmox dans le store CurrentUser (sans droits admin)
Write-Host "Connexion a Proxmox pour recuperer le certificat CA..." -ForegroundColor Cyan

try {
    $tcpClient = New-Object System.Net.Sockets.TcpClient("10.32.154.240", 8006)
    $callback = [System.Net.Security.RemoteCertificateValidationCallback]{ $true }
    $sslStream = New-Object System.Net.Security.SslStream($tcpClient.GetStream(), $false, $callback)
    $sslStream.AuthenticateAsClient("10.32.154.240")
    
    $cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2($sslStream.RemoteCertificate)
    $sslStream.Close()
    $tcpClient.Close()

    # Construire la chaine pour trouver la CA racine
    $chain = New-Object System.Security.Cryptography.X509Certificates.X509Chain
    $chain.ChainPolicy.RevocationMode = "NoCheck"
    $chain.ChainPolicy.VerificationFlags = "AllFlags"
    $chain.Build($cert) | Out-Null
    $rootCA = $chain.ChainElements[$chain.ChainElements.Count - 1].Certificate

    Write-Host "CA trouvee: $($rootCA.Subject)" -ForegroundColor Yellow

    # Import dans CurrentUser\Root (pas d'admin requis)
    $store = New-Object System.Security.Cryptography.X509Certificates.X509Store("Root", "CurrentUser")
    $store.Open("ReadWrite")
    $store.Add($rootCA)
    $store.Close()

    Write-Host "OK - Certificat importe dans CurrentUser\Trusted Root" -ForegroundColor Green
    Write-Host "Ferme et reouvre Chrome -> plus d'avertissement HTTPS" -ForegroundColor Green
} catch {
    Write-Host "Erreur: $_" -ForegroundColor Red
}

Read-Host "Appuie sur Entree pour fermer"
