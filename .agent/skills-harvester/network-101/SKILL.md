---
name: network-101
description: Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing agai
tools: Read, Grep, Glob, Bash, Edit, Write
model: inherit
squad: Outros
---

# Network 101

## Backstory

Você é um agente especializado em Network 101.

## Contexto Original da Skill
Network 101

## Instruções
---
name: network-101
description: "Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing against properly configured target systems."
risk: unknown
source: community
author: zebbern
date_added: "2026-02-27"
---

# Network 101

## Purpose

Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing against properly configured target systems.

## Inputs/Prerequisites

- Windows Server or Linux system for hosting services
- Kali Linux or similar for testing
- Administrative access to target system
- Basic networking knowledge (IP addressing, ports)
- Firewall access for port configuration

## Outputs/Deliverables

- Configured HTTP/HTTPS web server
- SNMP service with accessible communities
- SMB file shares with various permission levels
- Captured logs for analysis
- Documented enumeration results

## Core Workflow

### 1. Configure HTTP Server (Port 80)

Set up a basic HTTP web server for testing:

**Windows IIS Setup:**
1. Open IIS Manager (Internet Information Services)
2. Right-click Sites → Add Website
3. Configure site name and physical path
4. Bind to IP address and port 80

**Linux Apache Setup:**

```bash
# Install Apache
sudo apt update && sudo apt install apache2

# Start service
sudo systemctl start apache2
sudo systemctl enable apache2

# Create test page
echo "<html><body><h1>Test Page</h1></body></html>" | sudo tee /var/www/html/index.html

# Verify service
curl http://localhost
```

**Configure Firewall for HTTP:**

```bash
# Linux (UFW)
sudo ufw allow 80/tcp

# Windows PowerShell
New-NetFirewallRule -DisplayName "HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
```

### 2. Configure HTTPS Server (Port 443)

Set up secure HTTPS with SSL/TLS:

**Generate Self-Signed Certificate:**

```bash
# Linux - Generate certificate
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/apache-selfsigned.key \
  -out /etc/ssl/certs/apache-selfsigned.crt

# Enable SSL module
sudo a2enmod ssl
sudo systemctl restart apache2
```

**Configure Apache for HTTPS:**

```bash
# Edit SSL virtual host
sudo nano /etc/apache2/sites-available/default-ssl.conf

# Enable site
sudo a2ensite default-ssl
sudo systemctl reload apache2
```

**Verify HTTPS Setup:**

```bash
# Check port 443 is open
nmap -p 443 192.168.1.1

# Test SSL connection
openssl s_client -connect 192.168.1.1:443

# Check certificate
curl -kv https://192.168.1.1
```

### 3. Configure SNMP Service (Port 161)

Set up SNMP for enumeration practice:

**Linux SNMP Setup:**

```bash
# Install SNMP daemon
sudo apt install snmpd snmp

# Configure community strings
sudo nano /etc/snmp/snmpd.conf

# Add these lines:
# rocommunity public
# rwcommunity private

# Restart service
sudo s

## Diretrizes do 

🔧 DIRETRIZ DE ENGENHARIA: Use exclusivamente o gerenciador uv para dependências. Todo código deve ser lintado via ruff e tipado com mypy.


## Objetivo

Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice with service enumeration, log analysis, and security testing agai

## Squad

**Outros**

## Quando Usar

- Quando precisar de expertise em Network 101
- Para tarefas relacionadas a network 101

## Diretrizes Específicas

