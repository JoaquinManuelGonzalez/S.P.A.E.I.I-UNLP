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
              <input v-model="formData.alumno.email" id="email" type="email" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su nombre">
            </div>
            <div>
              <label for="genero" class="block text-sm font-medium text-gray-700">Género conforme pasaporte</label>
              <select v-model="formData.alumno.genero" id="genero" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                <option value="">Seleccione su género conforme pasaporte</option>
                <option value="masculino">Masculino</option>
                <option value="femenino">Femenino</option>
                <option value="otro">Otro</option>
              </select>
            </div>
            <div class="mb-4">
              <label for="fecha_de_nacimiento" class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
              <input v-model="formData.alumno.fecha_de_nacimiento" id="fecha_de_nacimiento" type="date" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su fecha de nacimiento">
            </div>
            <div class="mb-4">
              <label for="pais_de_nacimiento" class="block text-sm font-medium text-gray-700">País de nacimiento</label>
              <select v-model="formData.alumno.pais_de_nacimiento" id="pais_de_nacimiento" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                <option value="">Seleccione su país de nacimiento</option>
                <option value="Argentina">Argentina</option>
                <option value="Chile">Chile</option>
                <option value="Colombia">Colombia</option>
                <option value="Perú">Perú</option>
                <option value="Venezuela">Venezuela</option>
              </select>
            </div>
            <div class="mb-4">
              <label for="paisResidencia" class="block text-sm font-medium text-gray-700">País de residencia</label>
              <select v-model="formData.alumno.paisResidencia" id="paisResidencia" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                <option value="">Seleccione su país de residencia</option>
                <option value="Argentina">Argentina</option>
                <option value="Chile">Chile</option>
                <option value="Colombia">Colombia</option>
                <option value="Perú">Perú</option>
                <option value="Venezuela">Venezuela</option>
              </select>
            </div>
            <div class="mb-4">
              <label for="domicilio_pais_de_residencia" class="block text-sm font-medium text-gray-700">Domicilio del país de residencia</label>
              <input v-model="formData.alumno.domicilio_pais_de_residencia" id="domicilio_pais_de_residencia" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su domicilio del país de residencia">
            </div>
            <div class="mb-4">
              <label for="nacionalidad" class="block text-sm font-medium text-gray-700">Nacionalidad</label>
              <input v-model="formData.alumno.nacionalidad" id="nacionalidad" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su nacionalidad">
            </div>
            <div>
              <div class="mb-4">
                <label for="pasaporte" class="block text-sm font-medium text-gray-700">Pasaporte</label>
                <input v-model="formData.pasaporte.numero" id="pasaporte" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su número de pasaporte">
              </div>
              <div class="mb-4">
                <label for="paisEmisionPasaporte" class="block text-sm font-medium text-gray-700"> País de emisión de pasaporte</label>
                <select v-model="formData.pasaporte.pais_emision" id="paisEmisionPasaporte" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                  <option value="">Seleccione su país de emisión de pasaporte</option>
                  <option value="Argentina">Argentina</option>
                  <option value="Chile">Chile</option>
                  <option value="Colombia">Colombia</option>
                  <option value="Perú">Perú</option>
                  <option value="Venezuela">Venezuela</option>
                </select>
              </div>
              <div class="mb-4">
                <label for="fotoPasaporte" class="block text-sm font-medium text-gray-700">Foto/Archivo de pasaporte</label>
                <input v-on:change="onFileChange($event, 'fotoPasaporte')" id="fotoPasaporte" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
              </div>
            </div>
            <div>
              <div class="mb-4">
                <label for="cedulaIdentidad" class="block text-sm font-medium text-gray-700">Cédula de identidad</label>
                <input v-model="formData.cedula_de_identidad.numero" id="cedulaIdentidad" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su número de cédula de identidad">
              </div>
              <div class="mb-4">
                <label for="paisEmisionCedulaIdentidad" class="block text-sm font-medium text-gray-700"> País de emisión de cédula de identidad</label>
                <select v-model="formData.cedula_de_identidad.pais_emision" id="paisEmisionCedulaIdentidad" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                  <option value="">Seleccione su país de emisión de cédula de identidad</option>
                  <option value="Argentina">Argentina</option>
                  <option value="Chile">Chile</option>
                  <option value="Colombia">Colombia</option>
                  <option value="Perú">Perú</option>
                  <option value="Venezuela">Venezuela</option>
                </select>
              </div>
              <div class="mb-4">
                <label for="fotoCedulaIdentidad" class="block text-sm font-medium text-gray-700">Foto/Archivo de cédula de identidad</label>
                <input v-on:change="onFileChange($event, 'fotoCedulaIdentidad')" id="fotoCedulaIdentidad" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
              </div>
            </div>
            <div class="mb-4">
              <label for="estadoCivil" class="block text-sm font-medium text-gray-700">Estado Civil</label>
              <select v-model="formData.alumno.estadoCivil" id="estadoCivil" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                <option value="">Seleccione su estado civil</option>
                <option value="soltero">Soltero/a</option>
                <option value="casado">Casado/a</option>
                <option value="divorciado">Divorciado/a</option>
                <option value="viudo">Viudo/a</option>
              </select>
            </div>
            <div class="mb-4">
              <label for="certificadoB1" class="block text-sm font-medium text-gray-700">Certificado B1 o superior de español</label>
              <input v-on:change="onFileChange($event, 'certificadoB1')" id="certificadoB1" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
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
              <input v-model="formData.institucion.nivelEstudio" id="grado" name="nivelEstudio" type="radio" class="" required value="grado">
              <label for="grado" class="ml-1 text-sm font-normal text-gray-700">Estudiante de grado</label>
              <input v-model="formData.institucion.nivelEstudio" id="posgrado" name="nivelEstudio" type="radio" class="" required value="posgrado">
              <label for="posgrado" class="ml-1 text-sm font-normal text-gray-700">Estudiante de posgrado</label>
            </div>
            <div class="mb-4">
              <label for="planTrabajo" class="block text-sm font-medium text-gray-700">Foto/Archivo del plan de trabajo</label>
              <input v-on:change="onFileChange($event, 'planTrabajo')" id="planTrabajo" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
            </div>
            <div class="mb-4">
              <label for="consulado_visacion" class="block text-sm font-medium text-gray-700">Consulado de visación</label>
              <input v-model="formData.postulacion.consulado_visacion" id="consulado_visacion" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required placeholder="Ingrese su consulado de visación">
            </div>
            <div class="mb-4">
              <p class="block text-sm font-medium text-gray-700">Desea postularse por</p>
              <input v-model="formData.institucion.convenioPrograma" id="convenioUniversitario" name="convenioPrograma" type="radio" class="" required value="convenio">
              <label for="convenioUniversitario" class="ml-1 text-sm font-normal text-gray-700">Convenio universitario</label>
              <input v-model="formData.institucion.convenioPrograma" id="programa" name="convenioPrograma" type="radio" class="" required value="programa">
              <label for="programa" class="ml-1 text-sm font-normal text-gray-700">Programa estudiantil</label>
              <p class="mt-1 text-xs font-normal text-gray-700">Puede ver los Convenios que posee la Universidda Nacional de La Plata visitando el siguiente enlace: <a href=""></a></p>
            </div>
            <div class="mb-4">
              <label for="convenio" class="block text-sm font-medium text-gray-700">Convenio Universitario</label>
              <input v-model="formData.postulacion.convenio" id="convenio" type="text" class="mt-1 p-2 border border-gray-300 rounded-md w-full" placeholder="Ingrese su convenio universitario">
            </div>
            <div class="mb-4">
              <label for="nombre_programa" class="block text-sm font-medium text-gray-700">Programa estudiantil</label>
              <select v-model="formData.programa.nombre" id="nombre_programa" class="mt-1 p-2 border border-gray-300 rounded-md w-full">
                <option value="">Seleccione su programa</option>
                <option value="programa1">Programa 1</option>
                <option value="programa2">Programa 2</option>
              </select>
            </div>
            <div class="mb-4">
              <label for="cartaRecomendacion" class="block text-sm font-medium text-gray-700">Carta de recomendación de su universidad de origen</label>
              <input v-on:change="onFileChange($event, 'cartaRecomendacion')" id="cartaRecomendacion" type="file" class="mt-1 p-2 border border-gray-300 rounded-md w-full" required>
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
  
  <script>
  export default {
    data() {
      return {
        formData: {
          alumno: {
            apellido: "",
            nombre: "",
            email: "",
            domicilio_domicilio_pais_residencia: "",
            fecha_de_nacimiento: "",
            


            id_genero: "",
            id_estado_civil: "",
            id_pais_de_nacimiento: "",
            id_pais_de_residencia: "",
            id_pais_nacionalidad: "",


            pais_de_nacimiento: "",
            genero: "",
            paisResidencia: "",
            nacionalidad: "",
            estadoCivil: "",
            certificadoB1: null,
          },
          postulacion: {
            de_posgrado: false,
            universidad_origen: "",
            consulado_visacion: "",
            convenio: "",
          },
          programa: {
            nombre: "",
          },
          institucion: {
            nivelEstudio: "",
            planTrabajo: null,
            convenioPrograma: "",
            cartaRecomendacion: "",
          },
          tutorInstitucional: {
            nombre: "",
            apellido: "",
            email: "",
            es_institucional: true,
          },
          tutorAcademico: {
            nombre: "",
            apellido: "",
            email: "",
            es_institucional: false,
          },
          cedula_de_identidad: {
            numero: "",
            pais_emision: "",
            foto: null,
          },
          pasaporte: {
            numero: "",
            pais_emision: "",
            foto: null,
          }
        },
      };
    },
    methods: {
      submitForm() {
        console.log("Formulario enviado", this.formData);
      },
      onFileChange(event, key) {
        const file = event.target.files[0];
        switch(key){
          case 'fotoPasaporte':
            this.formData.pasaporte.foto = file;
            break;
          case 'fotoCedulaIdentidad':
            this.formData.cedula_de_identidad.foto = file;
            break;
          case 'certificadoB1':
            this.formData.alumno.certificadoB1 = file;
            break;
          case 'planTrabajo':
            this.formData.institucion.planTrabajo = file;
            break;
          case 'cartaRecomendacion':
            this.formData.institucion.cartaRecomendacion = file;
            break;
        }
      },
    },
  };
  </script>