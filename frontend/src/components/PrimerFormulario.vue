<template>
    <section class="p-6 max-w-4xl mx-auto bg-white rounded-lg shadow-lg">
      <h2 class="text-xl font-semibold text-center mb-4">Formulario de Postulación</h2>
      
      <form @submit.prevent="submitForm">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Datos Personales -->
          <div>
            <h3 class="font-semibold text-lg mb-2">Datos Personales</h3>
            <div class="mb-4">
              <label for="apellido" class="block text-sm font-medium text-gray-700">Apellido</label>
              <input v-model="formData.alumno.apellido" id="apellido" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su apellido">
            </div>
            <div class="mb-4">
              <label for="nombre" class="block text-sm font-medium text-gray-700">Nombre</label>
              <input v-model="formData.alumno.nombre" id="nombre" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su nombre">
            </div>
            <div class="mb-4">
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input v-model="formData.alumno.email" id="email" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su email">
            </div>
            <div class="mb-4">
              <label for="genero" class="block text-sm font-medium text-gray-700">Género conforme pasaporte</label>
              <select v-model="formData.alumno.id_genero" id="genero" class="mt-1 p-2 border border-gray-300 rounded-md w-full"  required>
                <option value="">Seleccione su género</option>
                <option v-for="genero in filteredGeneros" :key="genero.id" :value="genero.id">
                  {{ genero.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="fecha_de_nacimiento" class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
              <input v-model="formData.alumno.fecha_de_nacimiento" id="fecha_de_nacimiento" type="date" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su fecha de nacimiento">
            </div>
            <div class="mb-4">
              <label for="pais_de_nacimiento" class="block text-sm font-medium text-gray-700">País de nacimiento</label>
              <input type="text" v-model="searchQuery" id="search_pais" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Escriba para buscar su país"/>
              <select v-model="formData.alumno.id_pais_de_nacimiento" id="pais_de_nacimiento" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">Seleccione su país de nacimiento</option>
                <option v-for="pais in filteredAndSearchedPaises" :key="pais.id" :value="pais.id">
                  {{ pais.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="paisResidencia" class="block text-sm font-medium text-gray-700">País de residencia</label>
              <select v-model="formData.alumno.id_pais_de_residencia" id="paisResidencia" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">Seleccione su país de residencia</option>
                <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                  {{ pais.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="domicilio_pais_de_residencia" class="block text-sm font-medium text-gray-700">Domicilio del país de residencia</label>
              <input v-model="formData.alumno.domicilio_pais_de_residencia" id="domicilio_pais_de_residencia" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su domicilio del país de residencia">
            </div>
            <div class="mb-4">
              <label for="nacionalidad" class="block text-sm font-medium text-gray-700">Nacionalidad</label>
              <select v-model="formData.alumno.id_pais_nacionalidad" v-on:change="esHispanohablante()" id="nacionalidad" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">Selecciona tu país</option>
                <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                  {{ pais.name }}
                </option>
              </select>
            </div>
            <div>
              <div class="mb-4">
                <label for="pasaporte" class="block text-sm font-medium text-gray-700">Pasaporte</label>
                <input v-model="formData.pasaporte.numero" id="pasaporte" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su número de pasaporte" :required="!mercosur || formData.cedula_de_identidad.numero === '' || formData.archivo.pasaporte != null || formData.pasaporte.id_pais != ''">
              </div>
              <div class="mb-4">
                <label for="paisEmisionPasaporte" class="block text-sm font-medium text-gray-700"> País de emisión de pasaporte</label>
                <select v-model="formData.pasaporte.id_pais" id="paisEmisionPasaporte" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="!mercosur || formData.pasaporte.numero != '' || formData.archivo.pasaporte != null">
                  <option value="">Selecciona tu país de emisión de pasaporte</option>
                  <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                    {{ pais.name }}
                  </option>
                </select>
              </div>
              <div class="mb-4">
                <label for="fotoPasaporte" class="block text-sm font-medium text-gray-700">Foto/Archivo de pasaporte</label>
                <input v-on:change="onFileChange($event, 'fotoPasaporte')" ref="formData.archivo.pasaporte" id="fotoPasaporte" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="!mercosur || formData.pasaporte.numero != '' || formData.pasaporte.id_pais != ''">
              </div>
            </div>
            <div v-if="mercosur">
              <div class="mb-4">
                <label for="cedulaIdentidad" class="block text-sm font-medium text-gray-700">Cédula de identidad</label>
                <input v-model="formData.cedula_de_identidad.numero" id="cedulaIdentidad" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su número de cédula de identidad" :required="formData.pasaporte.numero === '' || formData.archivo.cedula_de_identidad != null || formData.cedula_de_identidad.id_pais != ''">
              </div>
              <div class="mb-4">
                <label for="paisEmisionCedulaIdentidad" class="block text-sm font-medium text-gray-700"> País de emisión de cédula de identidad</label>
                <select v-model="formData.cedula_de_identidad.id_pais" id="paisEmisionCedulaIdentidad" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="formData.cedula_de_identidad.numero != '' || formData.archivo.cedula_de_identidad != null">
                  <option value="">Selecciona tu país de emisión de cédula de identidad</option>
                  <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                    {{ pais.name }}
                  </option>
                </select>
              </div>
              <div class="mb-4">
                <label for="fotoCedulaIdentidad" class="block text-sm font-medium text-gray-700">Foto/Archivo de cédula de identidad</label>
                <input v-on:change="onFileChange($event, 'fotoCedulaIdentidad')" ref="formData.archivo.cedula_de_identidad" id="fotoCedulaIdentidad" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="formData.cedula_de_identidad.numero != '' || formData.cedula_de_identidad.id_pais != ''">
              </div>
            </div>
            <div class="mb-4">
              <label for="estadoCivil" class="block text-sm font-medium text-gray-700">Estado Civil</label>
              <select v-model="formData.alumno.id_estado_civil" id="estadoCivil" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">Seleccione su estado civil</option>
                <option v-for="estado in filteredEstadosCiviles" :key="estado.id" :value="estado.id">
                  {{ estado.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="certificadoB1" class="block text-sm font-medium text-gray-700">Certificado B1 o superior de español</label>
              <input v-on:change="onFileChange($event, 'certificadoB1')" ref="formData.archivo.certificado_b1" id="certificadoB1" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="!es_hispanohablante">
            </div>
          </div>
  
          <!-- Datos Académicos -->
          <div>
            <h3 class="font-semibold text-lg mb-2">Datos Académicos</h3>
            <div class="mb-4">
              <label for="universidad_origen" class="block text-sm font-medium text-gray-700">Universidad de Origen</label>
              <input v-model="formData.postulacion.universidad_origen" id="universidad_origen" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su universidad de origen">
            </div>
            <div class="mb-4">
              <p class="block text-sm font-medium text-gray-700">Nivel de estudio</p>
              <input v-model="nivelEstudio" id="grado" name="nivelEstudio" type="radio" class="" required value="grado">
              <label for="grado" class="ml-1 text-sm font-normal text-gray-700">Estudiante de grado</label>
              <input v-model="nivelEstudio" id="posgrado" name="nivelEstudio" type="radio" class="ml-4" required value="posgrado">
              <label for="posgrado" class="ml-1 text-sm font-normal text-gray-700">Estudiante de posgrado</label>
            </div>
            <div v-if="nivelEstudio === 'posgrado'" class="mb-4">
              <label for="planTrabajo" class="block text-sm font-medium text-gray-700">Foto/Archivo del plan de trabajo</label>
              <input v-on:change="onFileChange($event, 'planTrabajo')" ref="formData.value.archivo.plan_trabajo" id="planTrabajo" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="nivelEstudio === 'posgrado'">
            </div>
            <div class="mb-4">
              <label for="consulado_visacion" class="block text-sm font-medium text-gray-700">Consulado de visación</label>
              <input v-model="formData.postulacion.consulado_visacion" id="consulado_visacion" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su consulado de visación" :required="nivelEstudio === 'grado'">
            </div>
            <div class="mb-4">
              <p class="block text-sm font-medium text-gray-700">Desea postularse por</p>
              <input v-model="convenioPrograma" id="convenioUniversitario" name="convenioPrograma" type="radio" class="" required value="convenio">
              <label for="convenioUniversitario" class="ml-1 text-sm font-normal text-gray-700">Convenio universitario</label>
              <input v-model="convenioPrograma" id="programa" name="convenioPrograma" type="radio" class="ml-4" required value="programa">
              <label for="programa" class="ml-1 text-sm font-normal text-gray-700">Programa estudiantil</label>
              <p class="mt-1 text-xs font-normal text-gray-700">Puede ver los Convenios que posee la Universidda Nacional de La Plata visitando haciendo click <a href="https://conveniosunlp.presi.unlp.edu.ar/convenios" class="text-blue-500">aquí</a></p>
            </div>
            <div v-if="convenioPrograma === 'convenio'" class="mb-4">
              <label for="convenio" class="block text-sm font-medium text-gray-700">Convenio Universitario</label>
              <input v-model="formData.postulacion.convenio" id="convenio" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su convenio universitario" :required="convenioPrograma === 'convenio'">
            </div>
            <div v-if="convenioPrograma === 'programa'" class="mb-4">
              <label for="nombre_programa" class="block text-sm font-medium text-gray-700">Programa estudiantil</label>
              <select v-model="formData.id_programa" id="nombre_programa" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="convenioPrograma === 'programa'">
                <option value="">Seleccione su programa</option>
                <option v-for="programa in programas" :key="programa.id" :value="programa.id">
                  {{ programa.nombre }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="cartaRecomendacion" class="block text-sm font-medium text-gray-700">Carta de recomendación de su universidad de origen</label>
              <input v-on:change="onFileChange($event, 'cartaRecomendacion')" ref="formData.value.archivo.carta_recomendacion" id="cartaRecomendacion" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
            </div>
            <!-- Datos de Tutores -->
            <h3 class="font-semibold text-lg mb-2">Datos de Tutores</h3>
            <div class="mb-4">
              <label for="apellidoTutorInstitucional" class="block text-sm font-medium text-gray-700">Apellido de tutor institucional</label>
              <input v-model="formData.tutorInstitucional.apellido" id="apellidoTutorInstitucional" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese el apellido del tutor institucional">
            </div>
            <div class="mb-4">
              <label for="nombreTutorInstitucional" class="block text-sm font-medium text-gray-700">Nombre de tutor institucional</label>
              <input v-model="formData.tutorInstitucional.nombre" id="nombreTutorInstitucional" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese el nombre del tutor institucional">
            </div>
            <div class="mb-4">
              <label for="emailTutorInstitucional" class="block text-sm font-medium text-gray-700">Email de tutor institucional</label>
              <input v-model="formData.tutorInstitucional.email" id="emailTutoInstitucional" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese el email del tutor institucional">
            </div>
            <div class="mb-4">
              <label for="apellidoTutorAcademico" class="block text-sm font-medium text-gray-700">Apellido de tutor académico</label>
              <input v-model="formData.tutorAcademico.apellido" id="apellidoTutorAcademico" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese el apellido del tutor académico">
            </div>
            <div>
              <label for="nombreTutorAcademico" class="block text-sm font-medium text-gray-700">Nombre de tutor académico</label>
              <input v-model="formData.tutorAcademico.nombre" id="nombreTutorAcademico" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese el apellido del tutor académico">
            </div>
            <div class="mb-4">
              <label for="emailTutorAcademico" class="block text-sm font-medium text-gray-700">Email de tutor académico</label>
              <input v-model="formData.tutorAcademico.email" id="emailTutorAcademico" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese el email del tutor académico">
            </div>
          </div>
        </div>
  
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600">Postularme</button>
        </div>
      </form>
    </section>
  </template>


<script setup>
  import { onMounted, ref, computed } from 'vue';
  import { storeToRefs } from 'pinia';
  import { useI18n } from 'vue-i18n';
  import { usePrimerFormularioStore } from '../stores/PrimerFormularioStore';
  import  router from '../router';

  const store = usePrimerFormularioStore();
  const { formData, errors, loading, paises, estados_civiles, programas, generos, nivelEstudio, convenioPrograma, es_hispanohablante, mercosur } = storeToRefs(store);
  let searchQuery = ref('');
  // Accedemos al idioma actual a través de i18n
  const { locale } = useI18n();

  // Computed properties para filtrar las opciones según el idioma actual
  const filteredPaises = computed(() => {
    const currentLocale = locale.value; // El idioma actual
    //console.log(paises.value);
    console.log(currentLocale);
    const countries = paises.value.map(pais => ({
      id: pais.id,
      name: pais[`nombre_${currentLocale}`], // Usamos el nombre en el idioma actual
      hispanohablante: pais.hispanohablante
    }));
    console.log("el pais con id 1 es")
    console.log(paises.value);
    return countries;
  });

  const filteredEstadosCiviles = computed(() => {
    const currentLocale = locale.value;
    return estados_civiles.value.map(estado => ({
      id: estado.id,
      name: estado[`nombre_${currentLocale}`], // Usamos el nombre en el idioma actual
    }));
  });

  const filteredGeneros = computed(() => {
    const currentLocale = locale.value;
    return generos.value.map(genero => ({
      id: genero.id,
      name: genero[`nombre_${currentLocale}`], // Usamos el nombre en el idioma actual
    }));
  });

  const filteredAndSearchedPaises = computed(() => {
    const query = searchQuery.value.toLowerCase();
    return filteredPaises.value.filter(pais => pais.name.toLowerCase().includes(query));
  });

  // Cargar los datos cuando el componente se monta
  onMounted(() => {
    store.getData();
  });

  // Enviar el formulario
  const submitForm = async () => {
    console.log(formData);
    console.log(nivelEstudio);
    //await store.submitForm();
    if(nivelEstudio.value === 'posgrado'){
      formData.value.postulacion.de_posgrado = true;
    }
    formData.value.convenioPrograma = convenioPrograma.value;
    formData.value.mercosur = mercosur.value;
    try {
      console.log("Entra al try");
      if(validar()){
        console.log("arriba del submit");
        await store.submitForm();
        console.log("abajo del submit");
        router.push("/");
        alert("Formulario enviado con éxito");
      }
    } catch (error) {
      console.log(error);
      alert("Error al enviar el formulario");
    }
  };

  // Manejo de cambio de archivo
  const onFileChange = (event, key) => {
    const file = event.target.files[0];
    console.log(file);
    console.log(file.name);
    switch(key){
      case 'fotoPasaporte':
        formData.value.archivo.pasaporte = file;
        formData.value.titulos.titulo_pasaporte = file.name;
        break;
      case 'fotoCedulaIdentidad':
        formData.value.archivo.cedula_de_identidad = file;
        formData.value.titulos.titulo_cedula_de_identidad = file.name;
        break;
      case 'certificadoB1':
        formData.value.archivo.certificado_b1 = file;
        formData.value.titulos.titulo_certificado_b1 = file.name;
        break;
      case 'planTrabajo':
        formData.value.archivo.plan_trabajo = file;
        formData.value.titulos.titulo_plan_trabajo = file.name;
        break;
      case 'cartaRecomendacion':
        formData.value.archivo.carta_recomendacion = file;
        formData.value.titulos.titulo_carta_recomendacion = file.name;
        break;
    }
  };

  const esHispanohablante = () => {
    es_hispanohablante.value = paises.value[formData.value.alumno.id_pais_nacionalidad - 1].hispanohablante;
    let paises_mercosur = [42 /*Perú*/, 62 /*Colombia*/, 90 /*Paraguay*/, 125 /*Argentina*/, 150 /*Surinam*/, 166 /*Guyana*/, 169 /*Uruguay*/, 176 /*Panama*/, 202 /*Bolivia*/, 203 /*Chile*/, 210 /*Ecuador*/, 223 /*Brasil*/, 228 /*Venexuela*/]
    let nombres_mercosur = ["Perú", "Colombia", "Paraguay", "Argentina", "Surinam", "Guyana", "Uruguay", "Panamá", "Bolivia", "Chile", "Ecuador", "Brasil", "Venezuela"]
    let nombre = paises.value[formData.value.alumno.id_pais_nacionalidad - 1].nombre_es;
    mercosur.value = paises_mercosur.includes(formData.value.alumno.id_pais_nacionalidad);
  }

  const soloLetras = (valor) => {
    return /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(valor);
  }

  const validarArchivo = (archivo) => {
    const allowedExtensions = ['.pdf', '.jpg', '.jpeg', '.png'];
    const fileExtension = archivo.name.slice(archivo.name.lastIndexOf('.')).toLowerCase();
    return allowedExtensions.includes(fileExtension);
  }

  const soloNumeros = (value) => /^[0-9]+$/.test(value);

  const numerosLetras = (value) => /^[a-zA-Z0-9]+$/.test(value);

  const validar = () => {
    errors.value = [];
    if(formData.value.alumno.apellido.length < 3 || formData.value.alumno.apellido.length > 50 || !soloLetras(formData.value.alumno.apellido)){
      errors["apellido"] = "El apellido debe contener solo letras. Como mínimo 3 y como máximo 50 caracteres";
      alert(errors["apellido"]);
      return false;
    }
    if(formData.value.alumno.nombre.length < 3 || formData.value.alumno.nombre.length > 50 || !soloLetras(formData.value.alumno.nombre)){
      errors["nombre"] = "El nombre debe contener solo letras. Como mínimo 3 y como máximo 50 caracteres";
      alert(errors["nombre"]);
      return false;
    }
    if(formData.value.alumno.email.length < 3 || formData.value.alumno.email.length > 50){
      errors["email"] = "El email debe tener al menos 3 caracteres y como máximo 50 caracteres";
      alert(errors["email"]);
      return false;
    }
    if(formData.value.pasaporte.numero != "" && !numerosLetras(formData.value.pasaporte.numero)){
      errors["numero_pasaporte"] = "El pasaporte solo debe contener números y letras";
      alert(errors["numero_pasaporte"]);
      return false;
    }
    if(formData.value.archivo.pasaporte != null){
      if(!validarArchivo(formData.value.archivo.pasaporte)){
        errors["archivo_pasaporte"] = "Formato de archivo no válido. Solo se permiten archivos .pdf, .jpg, .jpeg, .png";
        alert(errors["archivo_pasaporte"]);
        return false;
      }
    }
    if(mercosur.value){
      if(formData.value.cedula_de_identidad.numero != "" && !soloNumeros(formData.value.cedula_de_identidad.numero)){
        errors["numero_cedula_de_identidad"] = "La cédula de identidad solo debe contener números";
        alert(errors["numero_cedula_de_identidad"]);
        return false;
      }
      if(formData.value.archivo.cedula_de_identidad != null){
        if(!validarArchivo(formData.value.archivo.cedula_de_identidad)){
          errors["archivo_cedula_de_identidad"] = "Formato de archivo no válido. Solo se permiten archivos .pdf, .jpg, .jpeg, .png";
          alert(errors["archivo_cedula_de_identidad"]);
          return false;
        }
      }
    }
    if(formData.value.archivo.certificado_b1 != null){
      if(!validarArchivo(formData.value.archivo.certificado_b1)){
        errors["archivo_certificado_b1"] = "Formato de archivo no válido. Solo se permiten archivos .pdf, .jpg, .jpeg, .png";
        alert(errors["archivo_certificado_b1"]);
        return false;
      }
    }
    if(nivelEstudio === 'posgrado'){
      if(formData.value.archivo.plan_trabajo != null){
        if(!validarArchivo(formData.value.archivo.plan_trabajo)){
          errors["archivo_plan_trabajo"] = "Formato de archivo no válido. Solo se permiten archivos .pdf, .jpg, .jpeg, .png";
          alert(errors["archivo_plan_trabajo"]);
          return false;
        }
      }
    }
    if(formData.value.archivo.carta_recomendacion != null){
      if(!validarArchivo(formData.value.archivo.carta_recomendacion)){
        errors["archivo_carta_recomendacion"] = "Formato de archivo no válido. Solo se permiten archivos .pdf, .jpg, .jpeg, .png";
        alert(errors["archivo_carta_recomendacion"]);
        return false;
      }
    }
    if(formData.value.postulacion.universidad_origen.length < 3 || formData.value.postulacion.universidad_origen.length > 50){
      errors["universidad_origen"] = "La universidad de origen debe tener al menos 3 caracteres y como máximo 50 caracteres";
      alert("La universidad de origen debe tener al menos 3 caracteres y como máximo 50 caracteres");
      return false;
    }
    if(formData.value.postulacion.consulado_visacion.length > 50){
      errors["consulado_visacion"] = "El consulado de visación debe tener como máximo 50 caracteres";
      alert(errors["consulado_visacion"]);
      return false;
    }
    if(formData.value.tutorInstitucional.apellido.length < 3 || formData.value.tutorInstitucional.apellido.length > 50 || !soloLetras(formData.value.tutorInstitucional.apellido)){
      errors["apellido_tutor_institucional"] = "El apellido del tutor institucional debe contener solo letras. Como mínimo 3 y como máximo 50 caracteres";
      alert(errors["apellido_tutor_institucional"]);
      return false;
    }
    if(formData.value.tutorInstitucional.nombre.length < 3 || formData.value.tutorInstitucional.nombre.length > 50 || !soloLetras(formData.value.tutorInstitucional.nombre)){
      errors["nombre_tutor_institucional"] = "El nombre del tutor institucional debe contener solo letras. Como mínimo 3 y como máximo 50 caracteres";
      alert(errors["nombre_tutor_institucional"]);
      return false;
    }
    if(formData.value.tutorInstitucional.email.length < 3 || formData.value.tutorInstitucional.email.length > 50){
      errors["email_tutor_institucional"] = "El email del tutor institucional debe tener al menos 3 caracteres y como máximo 50 caracteres";
      alert(errors["email_tutor_institucional"]);
      return false;
    }
    if(formData.value.tutorAcademico.apellido.length < 3 || formData.value.tutorAcademico.apellido.length > 50 || !soloLetras(formData.value.tutorAcademico.apellido)){
      errors["apellido_tutor_academico"] = "El apellido del tutor académico debe contener solo letras. Como mínimo 3 y como máximo 50 caracteres";
      alert(errors["apellido_tutor_academico"]);
      return false;
    }
    if(formData.value.tutorAcademico.nombre.length < 3 || formData.value.tutorAcademico.nombre.length > 50 || !soloLetras(formData.value.tutorAcademico.nombre)){
      errors["nombre_tutor_academico"] = "El nombre del tutor académico debe contener solo letras. Como mínimo 3 y como máximo 50 caracteres";
      alert(errors["nombre_tutor_academico"]);
      return false;
    }
    if(formData.value.tutorAcademico.email.length < 3 || formData.value.tutorAcademico.email.length > 50){
      errors["email_tutor_academico"] = "El email del tutor académico debe tener al menos 3 caracteres y como máximo 50 caracteres";
      alert(errors["email_tutor_academico"]);
      return false;
    }
    console.log(errors);
    return errors.value.length === 0;
    
  }

</script>


