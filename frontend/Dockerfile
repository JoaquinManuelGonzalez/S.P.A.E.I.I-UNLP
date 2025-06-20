# Etapa 1: Build de Vue con Node
FROM node:lts-alpine as build-stage

WORKDIR /app

# Copiamos dependencias e instalamos
COPY package*.json ./
RUN npm install

# Copiamos el resto del código y construimos
COPY . .
RUN npm run build

# Etapa 2: Servir los archivos con nginx
FROM nginx:stable-alpine as production-stage

# Eliminamos la configuración default de nginx y copiamos la nuestra
COPY nginx.conf /etc/nginx/nginx.conf

# Copiamos los archivos generados de la build de Vue
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Exponemos el puerto 80 para que sirva HTTP
EXPOSE 80

# Comando por defecto (ya viene por defecto, pero por claridad)
CMD ["nginx", "-g", "daemon off;"]
