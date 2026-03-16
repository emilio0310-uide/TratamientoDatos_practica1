# Secure Access API
## API REST para Evaluación de Riesgo de Accesos – Seguridad de la Información

---

## 1. Introducción

En el contexto actual de la seguridad de la información, el control y monitoreo de accesos a los sistemas es un componente fundamental para la protección de los activos digitales de una organización.  
El presente proyecto consiste en el diseño, construcción, contenerización y despliegue de un API REST funcional, orientado al registro y evaluación de intentos de acceso, aplicando buenas prácticas de desarrollo, versionamiento y despliegue en la nube.

El API ha sido desarrollado utilizando Python y el framework Flask, integrando mecanismos básicos de autenticación, validación de datos, cálculo de riesgo y registro de eventos para fines de auditoría.

---

## 2. Objetivo del Proyecto

Diseñar, construir, contenerizar y desplegar un API funcional que permita:
- Registrar intentos de acceso a un sistema.
- Evaluar el nivel de riesgo asociado a cada intento.
- Aplicar principios básicos de seguridad de la información.
- Desplegar el servicio en la nube y hacerlo accesible públicamente.

---

## 3. Tecnologías Utilizadas

- **Lenguaje:** Python  
- **Framework:** Flask  
- **Autenticación:** HTTP Basic Authentication  
- **Contenerización:** Docker  
- **Control de versiones:** Git y GitHub  
- **Pruebas de endpoints:** curl  
- **Despliegue en la nube:** Google Cloud Run  

---

## 4. Arquitectura de la Solución

La solución se basa en una arquitectura de tipo API REST, donde:
- El cliente consume los endpoints mediante solicitudes HTTP.
- El API valida los datos recibidos.
- Se autentican los usuarios antes de permitir el acceso al endpoint protegido.
- Se calcula un score de riesgo basado en reglas simples.
- Se registran logs estructurados para auditoría y monitoreo.
- El servicio se ejecuta dentro de un contenedor Docker desplegado en la nube.

---

## 5. Seguridad de la Información Implementada

El proyecto incorpora los siguientes controles de seguridad:
- Autenticación básica para proteger endpoints críticos.
- Validación de datos de entrada para prevenir errores y abusos.
- Clasificación de riesgo de accesos (scoring).
- Registro de eventos para trazabilidad y auditoría.
- Ejecución en entorno aislado mediante contenedores.

---

## 6. Endpoints del API

### 6.1 GET /health
Endpoint público utilizado para verificar el estado del servicio.

**Respuesta:**
```json
{
  "status": "ok"
}
