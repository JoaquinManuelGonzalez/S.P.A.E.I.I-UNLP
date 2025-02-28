<template>
    <section class="p-6 max-w-4xl mx-auto bg-white rounded-lg shadow-lg">
      <div v-if="periodo_activo">
        <h2 class="text-xl font-semibold text-center mb-4">{{ $t("formulario.titulos.titulo") }}</h2>
      </div>
      <div v-else>
        <h2 class="text-xl font-semibold text-center mb-4" style="color: red; font-size: x-large">{{ $t("formulario.extras.periodoInactivo") }}</h2>
        <p class="font-semibold text-lg mb-2" style="text-align: center;">{{ $t("formulario.extras.mensajePeriodoInactivo") }}</p>
      </div>
      
      <form @submit.prevent="submitForm">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Datos Personales -->
          <div>
            <h3 class="font-semibold text-lg mb-2">{{ $t("formulario.titulos.datosPersonales") }}</h3>
            <div class="mb-4">
              <label for="apellido" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.apellido") }}</label>
              <input v-model="formData.alumno.apellido" id="apellido" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.apellido')">
            </div>
            <div class="mb-4">
              <label for="nombre" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.nombre") }}</label>
              <input v-model="formData.alumno.nombre" id="nombre" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.nombre')">
            </div>
            <div class="mb-4">
              <label for="email" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.email") }}</label>
              <input v-model="formData.alumno.email" id="email" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.email')">
            </div>
            <div class="mb-4">
              <label for="genero" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.genero") }}</label>
              <select v-model="formData.alumno.id_genero" id="genero" class="mt-1 p-2 border border-gray-300 rounded-md w-full"  required>
                <option value="">{{ $t('formulario.placeholders.genero') }}</option>
                <option v-for="genero in filteredGeneros" :key="genero.id" :value="genero.id">
                  {{ genero.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="fecha_de_nacimiento" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.fechaNacimiento") }}</label>
              <input v-model="formData.alumno.fecha_de_nacimiento" id="fecha_de_nacimiento" type="date" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.fechaNacimiento')">
            </div>
            <div class="mb-4">
              <label for="pais_de_nacimiento" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.paisNacimiento") }}</label>
              <select v-model="formData.alumno.id_pais_de_nacimiento" id="pais_de_nacimiento" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">{{ $t("formulario.placeholders.paisNacimiento") }}</option>
                <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                  {{ pais.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="paisResidencia" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.paisResidencia") }}</label>
              <select v-model="formData.alumno.id_pais_de_residencia" id="paisResidencia" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">{{ $t('formulario.placeholders.paisResidencia') }}</option>
                <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                  {{ pais.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="domicilio_pais_de_residencia" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.domicilio") }}</label>
              <input v-model="formData.alumno.domicilio_pais_de_residencia" id="domicilio_pais_de_residencia" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.domicilio')">
            </div>
            <div class="mb-4">
              <label for="nacionalidad" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.nacionalidad") }}</label>
              <select v-model="formData.alumno.id_pais_nacionalidad" v-on:change="esHispanohablante()" id="nacionalidad" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">{{ $t('formulario.placeholders.nacionalidad') }}</option>
                <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                  {{ pais.name }}
                </option>
              </select>
            </div>
            <div>
              <div class="mb-4">
                <label for="pasaporte" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.pasaporte") }}</label>
                <input v-model="formData.pasaporte.numero" id="pasaporte" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :placeholder="$t('formulario.placeholders.pasaporte')" :required="!mercosur || formData.cedula_de_identidad.numero === '' || formData.archivo.pasaporte != null || formData.pasaporte.id_pais != ''">
              </div>
              <div class="mb-4">
                <label for="paisEmisionPasaporte" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.paisEmisionPasaporte") }}</label>
                <select v-model="formData.pasaporte.id_pais" id="paisEmisionPasaporte" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="!mercosur || formData.pasaporte.numero != '' || formData.archivo.pasaporte != null">
                  <option value="">{{ $t('formulario.placeholders.paisEmisionPasaporte') }}</option>
                  <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                    {{ pais.name }}
                  </option>
                </select>
              </div>
              <div class="mb-4">
                <label for="fotoPasaporte" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.archivoPasaporte") }}</label>
                <input v-on:change="onFileChange($event, 'fotoPasaporte')" ref="formData.archivo.pasaporte" id="fotoPasaporte" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="!mercosur || formData.pasaporte.numero != '' || formData.pasaporte.id_pais != ''">
              </div>
            </div>
            <div v-if="mercosur">
              <div class="mb-4">
                <label for="cedulaIdentidad" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.cedulaIdentidad") }}</label>
                <input v-model="formData.cedula_de_identidad.numero" id="cedulaIdentidad" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :placeholder="$t('formulario.placeholders.cedulaIdentidad')" :required="formData.pasaporte.numero === '' || formData.archivo.cedula_de_identidad != null || formData.cedula_de_identidad.id_pais != ''">
              </div>
              <div class="mb-4">
                <label for="paisEmisionCedulaIdentidad" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.paisEmisionCedula") }}</label>
                <select v-model="formData.cedula_de_identidad.id_pais" id="paisEmisionCedulaIdentidad" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="formData.cedula_de_identidad.numero != '' || formData.archivo.cedula_de_identidad != null">
                  <option value="">{{ $t('formulario.placeholders.paisEmisionCedula') }}</option>
                  <option v-for="pais in filteredPaises" :key="pais.id" :value="pais.id">
                    {{ pais.name }}
                  </option>
                </select>
              </div>
              <div class="mb-4">
                <label for="fotoCedulaIdentidad" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.archivoCedula") }}</label>
                <input v-on:change="onFileChange($event, 'fotoCedulaIdentidad')" ref="formData.archivo.cedula_de_identidad" id="fotoCedulaIdentidad" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :placeholder="$t('formulario.placeholders.archivoCedula')" :required="formData.cedula_de_identidad.numero != '' || formData.cedula_de_identidad.id_pais != ''">
              </div>
            </div>
            <div class="mb-4">
              <label for="estadoCivil" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.estadoCivil") }}</label>
              <select v-model="formData.alumno.id_estado_civil" id="estadoCivil" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
                <option value="">{{ $t('formulario.placeholders.estadoCivil') }}</option>
                <option v-for="estado in filteredEstadosCiviles" :key="estado.id" :value="estado.id">
                  {{ estado.name }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="certificadoB1" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.certificadoB1") }}</label>
              <input v-on:change="onFileChange($event, 'certificadoB1')" ref="formData.archivo.certificado_b1" id="certificadoB1" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="!es_hispanohablante">
            </div>
            <div class="mb-4">
              <input v-model="formData.alumno.discapacitado" id="checkDiscapacidad" type="checkbox" value="true">
              <label for="checkDiscapacidad" class="text-sm font-medium text-gray-700 ml-1">{{ $t("formulario.campos.checkDiscapacidad") }}</label>
            </div>
            <div v-if="formData.alumno.discapacitado" class="mb-4">
              <label for="certificadoDiscapacidad" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.certificadoDiscapacidad") }}</label>
              <input v-on:change="onFileChange($event, 'certificadoDiscapacidad')" ref="formData.value.archivo.certificadoDiscapacidad" id="certificadoDiscapacidad" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
            </div>
          </div>
  
          <!-- Datos Académicos -->
          <div>
            <h3 class="font-semibold text-lg mb-2">{{ $t("formulario.titulos.datosAcademicos") }}</h3>
            <div class="mb-4">
              <label for="universidad_origen" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.universidad") }}</label>
              <input v-model="formData.postulacion.universidad_origen" id="universidad_origen" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.universidad')">
            </div>
            <div class="mb-4">
              <p class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.nivelEstudios") }}</p>
              <input v-model="nivelEstudio" id="grado" name="nivelEstudio" type="radio" class="" required value="grado">
              <label for="grado" class="ml-1 text-sm font-normal text-gray-700">{{ $t('formulario.placeholders.grado') }}</label>
              <input v-model="nivelEstudio" id="posgrado" name="nivelEstudio" type="radio" class="ml-4" required value="posgrado">
              <label for="posgrado" class="ml-1 text-sm font-normal text-gray-700">{{ $t('formulario.placeholders.posgrado') }}</label>
            </div>
            <div v-if="nivelEstudio === 'posgrado'" class="mb-4">
              <label for="planTrabajo" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.planTrabajo") }}</label>
              <input v-on:change="onFileChange($event, 'planTrabajo')" ref="formData.value.archivo.plan_trabajo" id="planTrabajo" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="nivelEstudio === 'posgrado'">
            </div>
            <div class="mb-4">
              <label for="consulado_visacion" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.consuladoVisacion") }}</label>
              <input v-model="formData.postulacion.consulado_visacion" id="consulado_visacion" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :placeholder="$t('formulario.placeholders.consuladoVisacion')" :required="nivelEstudio === 'grado'">
            </div>
            <div class="mb-4">
              <p class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.deseaPostularsePor") }}</p>
              <input v-model="convenioPrograma" id="convenioUniversitario" name="convenioPrograma" type="radio" class="" required value="convenio">
              <label for="convenioUniversitario" class="ml-1 text-sm font-normal text-gray-700"> {{ $t('formulario.placeholders.convenio') }}</label>
              <input v-model="convenioPrograma" id="programa" name="convenioPrograma" type="radio" class="ml-4" required value="programa">
              <label for="programa" class="ml-1 text-sm font-normal text-gray-700">{{ $t('formulario.placeholders.programa') }}</label>
              <p class="mt-1 text-xs font-normal text-gray-700">{{ $t('formulario.extras.mensaje') }} <a href="https://conveniosunlp.presi.unlp.edu.ar/convenios" class="text-blue-500" target="_blank">{{ $t('formulario.extras.clickAqui') }}</a></p>
            </div>
            <div v-if="convenioPrograma === 'convenio'" class="mb-4">
              <label for="convenio" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.convenioUniversitario") }}</label>
              <input v-model="formData.postulacion.convenio" id="convenio" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :placeholder="$t('formulario.placeholders.convenioUniversitario')" :required="convenioPrograma === 'convenio'">
            </div>
            <div v-if="convenioPrograma === 'programa'" class="mb-4">
              <label for="nombre_programa" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.programaEstudiantil") }}</label>
              <select v-model="formData.id_programa" id="nombre_programa" class="mt-1 p-2 border border-gray-300 rounded-md w-full" :required="convenioPrograma === 'programa'">
                <option value="">{{ $t('formulario.placeholders.programaEstudiantil') }}</option>
                <option v-for="programa in programas" :key="programa.id" :value="programa.id">
                  {{ programa.nombre }}
                </option>
              </select>
            </div>
            <div class="mb-4">
              <label for="cartaRecomendacion" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.cartaRecomendacion") }}</label>
              <input v-on:change="onFileChange($event, 'cartaRecomendacion')" ref="formData.value.archivo.carta_recomendacion" id="cartaRecomendacion" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
            </div>
            <!-- Datos de Tutores -->
            <h3 class="font-semibold text-lg mb-2">{{ $t("formulario.titulos.datosTutores") }}</h3>
            <div class="mb-4">
              <label for="apellidoTutorInstitucional" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.apellidoTutorInstitucional") }}</label>
              <input v-model="formData.tutorInstitucional.apellido" id="apellidoTutorInstitucional" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.apellidoTutorInstitucional')">
            </div>
            <div class="mb-4">
              <label for="nombreTutorInstitucional" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.nombreTutorInstitucional") }}</label>
              <input v-model="formData.tutorInstitucional.nombre" id="nombreTutorInstitucional" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.nombreTutorInstitucional')">
            </div>
            <div class="mb-4">
              <label for="emailTutorInstitucional" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.emailTutorInstitucional") }}</label>
              <input v-model="formData.tutorInstitucional.email" id="emailTutoInstitucional" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.emailTutorInstitucional')">
            </div>
            <div class="mb-4">
              <label for="apellidoTutorAcademico" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.apellidoTutorAcademico") }}</label>
              <input v-model="formData.tutorAcademico.apellido" id="apellidoTutorAcademico" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.apellidoTutorAcademico')">
            </div>
            <div class="mb-4">
              <label for="nombreTutorAcademico" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.nombreTutorAcademico") }}</label>
              <input v-model="formData.tutorAcademico.nombre" id="nombreTutorAcademico" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.nombreTutorAcademico')">
            </div>
            <div class="mb-4">
              <label for="emailTutorAcademico" class="block text-sm font-medium text-gray-700">{{ $t("formulario.campos.emailTutorAcademico") }}</label>
              <input v-model="formData.tutorAcademico.email" id="emailTutorAcademico" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required :placeholder="$t('formulario.placeholders.emailTutorAcademico')">
            </div>
          </div>
        </div>
  
        <div v-if="periodo_activo" class="flex justify-center mt-6">
          <button type="submit" class="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600">{{ $t("formulario.extras.boton") }}</button>
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
  const { formData, errors, loading, paises, estados_civiles, programas, generos, nivelEstudio, convenioPrograma, es_hispanohablante, mercosur, periodo_activo } = storeToRefs(store);
  // Accedemos al idioma actual a través de i18n
  const { locale } = useI18n();
  const { t } = useI18n();

  // Computed properties para filtrar las opciones según el idioma actual
  const filteredPaises = computed(() => {
    const currentLocale = locale.value; // El idioma actual
    const countries = paises.value.map(pais => ({
      id: pais.id,
      name: pais[`nombre_${currentLocale}`], // Usamos el nombre en el idioma actual
      hispanohablante: pais.hispanohablante
    }));
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

  // Cargar los datos cuando el componente se monta
  onMounted(() => {
    store.getData();
  });

  // Enviar el formulario
  const submitForm = async () => {
    //await store.submitForm();
    if(nivelEstudio.value === 'posgrado'){
      formData.value.postulacion.de_posgrado = true;
    }
    formData.value.convenioPrograma = convenioPrograma.value;
    formData.value.mercosur = mercosur.value;
    try {
      if(validar()){
        await store.submitForm();
        router.push("/");
      }
    } catch (error) {
      alert("Error al enviar el formulario");
    }
  };

  // Manejo de cambio de archivo
  const onFileChange = (event, key) => {
    const file = event.target.files[0];
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
      case 'certificadoDiscapacidad':
        formData.value.archivo.certificadoDiscapacidad = file;
        formData.value.titulos.titulo_certificado_discapacidad = file.name;
        break;
    }
  };

  const esHispanohablante = () => {
    es_hispanohablante.value = paises.value[formData.value.alumno.id_pais_nacionalidad - 1].hispanohablante;
    let paises_mercosur = [42 /*Perú*/, 62 /*Colombia*/, 90 /*Paraguay*/, 125 /*Argentina*/, 150 /*Surinam*/, 166 /*Guyana*/, 169 /*Uruguay*/, 202 /*Bolivia*/, 203 /*Chile*/, 210 /*Ecuador*/, 223 /*Brasil*/, 228 /*Venezuela*/]
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

  const validarFecha = (fecha) => {
    const fechaSeleccionada = new Date(fecha); 
    const fechaActual = new Date(); 
    fechaActual.setHours(0, 0, 0, 0);
    fechaSeleccionada.setHours(0, 0, 0, 0);

    return fechaSeleccionada <= fechaActual;
  };

  const validar = () => {
    errors.value = [];
    if(formData.value.alumno.apellido.length < 2 || formData.value.alumno.apellido.length > 50 || !soloLetras(formData.value.alumno.apellido)){
      errors["apellido"] = t("formulario.errors.apellido");
      alert(errors["apellido"]);
      return false;
    }
    if(formData.value.alumno.nombre.length < 2 || formData.value.alumno.nombre.length > 50 || !soloLetras(formData.value.alumno.nombre)){
      errors["nombre"] = t("formulario.errors.nombre");
      alert(errors["nombre"]);
      return false;
    }
    if(formData.value.alumno.email.length < 3 || formData.value.alumno.email.length > 50){
      errors["email"] = t("formulario.errors.email");
      alert(errors["email"]);
      return false;
    }
    if(formData.value.pasaporte.numero != "" && !numerosLetras(formData.value.pasaporte.numero)){
      errors["numero_pasaporte"] = t("formulario.errors.numero_pasaporte");
      alert(errors["numero_pasaporte"]);
      return false;
    }
    if(formData.value.archivo.pasaporte != null){
      if(!validarArchivo(formData.value.archivo.pasaporte)){
        errors["archivo_pasaporte"] = t("formulario.errors.archivo_pasaporte");
        alert(errors["archivo_pasaporte"]);
        return false;
      }
    }
    if(mercosur.value){
      if(formData.value.cedula_de_identidad.numero != "" && !soloNumeros(formData.value.cedula_de_identidad.numero)){
        errors["numero_cedula_de_identidad"] = t("formulario.errors.numero_cedula_de_identidad");
        alert(errors["numero_cedula_de_identidad"]);
        return false;
      }
      if(formData.value.archivo.cedula_de_identidad != null){
        if(!validarArchivo(formData.value.archivo.cedula_de_identidad)){
          errors["archivo_cedula_de_identidad"] = t("formulario.errors.archivo_cedula");
          alert(errors["archivo_cedula_de_identidad"]);
          return false;
        }
      }
    }
    if(formData.value.archivo.certificado_b1 != null){
      if(!validarArchivo(formData.value.archivo.certificado_b1)){
        errors["archivo_certificado_b1"] = t("formulario.errors.certificado_b1");
        alert(errors["archivo_certificado_b1"]);
        return false;
      }
    }
    if(nivelEstudio === 'posgrado'){
      if(formData.value.archivo.plan_trabajo != null){
        if(!validarArchivo(formData.value.archivo.plan_trabajo)){
          errors["archivo_plan_trabajo"] = t("formulario.errors.plan_trabajo");
          alert(errors["archivo_plan_trabajo"]);
          return false;
        }
      }
    }
    if(formData.value.archivo.carta_recomendacion != null){
      if(!validarArchivo(formData.value.archivo.carta_recomendacion)){
        errors["archivo_carta_recomendacion"] = t("formulario.errors.carta_recomendacion");
        alert(errors["archivo_carta_recomendacion"]);
        return false;
      }
    }
    if(formData.value.postulacion.universidad_origen.length < 3 || formData.value.postulacion.universidad_origen.length > 50){
      errors["universidad_origen"] = t("formulario.errors.universidad_origen");
      alert(errors["universidad_origen"]);
      return false;
    }
    if(formData.value.postulacion.consulado_visacion.length > 50){
      errors["consulado_visacion"] = t("formulario.errors.consulado_visacion");
      alert(errors["consulado_visacion"]);
      return false;
    }
    if(formData.value.tutorInstitucional.apellido.length < 2 || formData.value.tutorInstitucional.apellido.length > 50 || !soloLetras(formData.value.tutorInstitucional.apellido)){
      errors["apellido_tutor_institucional"] = t("formulario.errors.apellido_tutor_institucional");
      alert(errors["apellido_tutor_institucional"]);
      return false;
    }
    if(formData.value.tutorInstitucional.nombre.length < 2 || formData.value.tutorInstitucional.nombre.length > 50 || !soloLetras(formData.value.tutorInstitucional.nombre)){
      errors["nombre_tutor_institucional"] = t("formulario.errors.nombre_tutor_institucional");
      alert(errors["nombre_tutor_institucional"]);
      return false;
    }
    if(formData.value.tutorInstitucional.email.length < 3 || formData.value.tutorInstitucional.email.length > 50){
      errors["email_tutor_institucional"] = t("formulario.errors.email_tutor_institucional");
      alert(errors["email_tutor_institucional"]);
      return false;
    }
    if(formData.value.tutorAcademico.apellido.length < 2 || formData.value.tutorAcademico.apellido.length > 50 || !soloLetras(formData.value.tutorAcademico.apellido)){
      errors["apellido_tutor_academico"] = t("formulario.errors.apellido_tutor_academico");
      alert(errors["apellido_tutor_academico"]);
      return false;
    }
    if(formData.value.tutorAcademico.nombre.length < 2 || formData.value.tutorAcademico.nombre.length > 50 || !soloLetras(formData.value.tutorAcademico.nombre)){
      errors["nombre_tutor_academico"] = t("formulario.errors.nombre_tutor_academico");
      alert(errors["nombre_tutor_academico"]);
      return false;
    }
    if(formData.value.tutorAcademico.email.length < 3 || formData.value.tutorAcademico.email.length > 50){
      errors["email_tutor_academico"] = t("formulario.errors.email_tutor_academico");
      alert(errors["email_tutor_academico"]);
      return false;
    }
    if(formData.value.alumno.fecha_de_nacimiento === "" || !validarFecha(formData.value.alumno.fecha_de_nacimiento)){
      errors["fecha_de_nacimiento"] = t("formulario.errors.fecha_de_nacimiento");
      alert(errors["fecha_de_nacimiento"]);
      return false;
    }
    return errors.value.length === 0;
    
  }

</script>


