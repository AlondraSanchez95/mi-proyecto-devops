#!/bin/bash
echo "Simulando despliegue del sitio web..."
echo "Archivos listos para produccion"
chmod +x scripts/deploy.sh
./scripts/deploy.sh
echo "Despliegue completado exitosamente"