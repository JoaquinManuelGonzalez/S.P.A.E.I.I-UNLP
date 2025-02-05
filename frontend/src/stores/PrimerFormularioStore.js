import { defineStore } from 'pinia'
import axios from 'axios';

export const usePrimerFormularioStore = defineStore('primer_formulario_store', {
    state: () => ({
        formData: {
            alumno: {
                apellido: "",
                nombre: "",
                email: "",
                domicilio_pais_de_residencia: "",
                fecha_de_nacimiento: "",
                
                id_genero: "",
                id_estado_civil: "",
                id_pais_de_nacimiento: "",
                id_pais_de_residencia: "",
                id_pais_nacionalidad: "",
            },
            postulacion: {
                de_posgrado: false,
                universidad_origen: "",
                consulado_visacion: "",
                convenio: "",
            },
            id_programa: "",
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
                id_pais: "",
            },
            pasaporte: {
                numero: "",
                id_pais: "",
            },
            archivo: {
                certificado_b1: null,
                plan_trabajo: null,
                carta_recomendacion: null,
                cedula_de_identidad: null,
                pasaporte: null,
            },
            titulos:{
                titulo_certificado_b1: "",
                titulo_plan_trabajo: "",
                titulo_carta_recomendacion: "",
                titulo_cedula_de_identidad: "",
                titulo_pasaporte: "",
            },
            convenioPrograma: "",
            mercosur: false,
        },
        errors: [],
        loading: false,
        paises: [],
        generos: [],
        estados_civiles: [],
        programas: [],
        nivelEstudio: "",
        convenioPrograma: "",
        es_hispanohablante: false,
        mercosur: false,
        csrf_token: "",
        periodo_activo: true,
    }),
    actions: {
        async submitForm() {
            this.loading = true;
            try {
                const archivos = this.formData.archivo;

                for (const key in archivos) {
                    if (archivos[key]) {
                        archivos[key] = await this.convertToBase64(archivos[key]);
                    }
                }
                const response = await axios.post('http://127.0.0.1:5000/api/postulacion/primer-formulario', this.formData, 
                    {
                        headers: {
                            'Content-Type': 'application/json',
                            //'X-CSRF-Token': this.csrf_token,
                        },
                    },
                );
                alert("Formulario enviado con éxito");
            } catch (error) {
                if(error.response){
                    this.errors = [error.response.data.error];
                    alert(error.response.data.error);
                }else{
                    alert("Error al enviar el formulario");
                }
            } finally {
                this.loading = false;
                this.limpiarFormulario();
            }
        },
        async getData(){
            this.loading = true;
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/postulacion/primer-formulario-data',
                );
                this.errors = null;
                this.estados_civiles = response.data.estados_civiles;
                this.generos = response.data.generos;
                this.paises = response.data.paises;
                this.csrf_token = response.data.csrf_token;
                this.programas = response.data.programas;
                this.periodo_activo = response.data.periodo_activo;
                console.log("estos son los paises");
                console.log(this.paises[1]);
            } catch (error) {
                this.errors = error.response.data;
            } finally {
                this.loading = false;
            }
        },
        async convertToBase64(file) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = () => resolve(reader.result.split(',')[1]); // Obtén solo la parte Base64
                reader.onerror = (error) => reject(error);
                reader.readAsDataURL(file);
            });
        },
        limpiarFormulario() {
            this.formData.alumno.apellido = "";
            this.formData.alumno.nombre = "";
            this.formData.alumno.email = "";
            this.formData.alumno.domicilio_pais_de_residencia = "";
            this.formData.alumno.fecha_de_nacimiento = "";
            this.formData.alumno.id_genero = "";
            this.formData.alumno.id_estado_civil = "";
            this.formData.alumno.id_pais_de_nacimiento = "";
            this.formData.alumno.id_pais_de_residencia = "";
            this.formData.alumno.id_pais_nacionalidad = "";
            this.formData.postulacion.de_posgrado = false;
            this.formData.postulacion.universidad_origen = "";
            this.formData.postulacion.consulado_visacion = "";
            this.formData.postulacion.convenio = "";
            this.formData.id_programa = "";
            this.formData.tutorInstitucional.nombre = "";
            this.formData.tutorInstitucional.apellido = "";
            this.formData.tutorInstitucional.email = "";
            this.formData.tutorInstitucional.es_institucional = true;
            this.formData.tutorAcademico.nombre = "";
            this.formData.tutorAcademico.apellido = "";
            this.formData.tutorAcademico.email = "";
            this.formData.tutorAcademico.es_institucional = false;
            this.formData.cedula_de_identidad.numero = "";
            this.formData.cedula_de_identidad.id_pais = "";
            this.formData.pasaporte.numero = "";
            this.formData.pasaporte.id_pais = "";
            this.formData.archivo.certificado_b1 = null;
            this.formData.archivo.plan_trabajo = null;
            this.formData.archivo.carta_recomendacion = null;
            this.formData.archivo.cedula_de_identidad = null;
            this.formData.archivo.pasaporte = null;
            this.formData.titulos.titulo_certificado_b1 = "";
            this.formData.titulos.titulo_plan_trabajo = "";
            this.formData.titulos.titulo_carta_recomendacion = "";
            this.formData.titulos.titulo_cedula_de_identidad = "";
            this.formData.titulos.titulo_pasaporte = "";
            this.formData.convenioPrograma = "";
            this.formData.mercosur = false;
            this.nivelEstudio = "";
            this.convenioPrograma = "";
            this.es_hispanohablante = false;
            this.mercosur = false;
        }
            
    },

});