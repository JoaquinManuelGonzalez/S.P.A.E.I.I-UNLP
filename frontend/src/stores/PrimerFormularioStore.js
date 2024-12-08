import { defineStore } from 'pinia'
import axios from 'axios'

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
        },
        errors: null,
        loading: false,
        paises: [],
        generos: [],
        estados_civiles: [],
        convenioPrograma: "",
        nivelEstudio: "",
        csrf_token: "",
    }),
    actions: {
        async submitForm() {
            this.loading = true;
            try {
                console.log("este es el form data:");
                console.log("holaaaaaa");
                console.log(this.formData);
                const response = await axios.post('http://127.0.0.1:5000/api/postulacion/primer-formulario', this.formData,
                    {
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": this.csrf_token,
                        },
                    }
                ).then(response => {
                    console.log(response);
                });
                this.errors = null;
                console.log("esta es la respuesta:");
                console.log(response);
                this.resetFormulario()
            } catch (error) {
                this.errors = error;
                console.log("este es el error:");
                console.log(error);
            } finally {
                this.loading = false;
            }
        },
        async getData(){
            this.loading = true;
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/postulacion/primer-formulario-data');
                this.errors = null;
                this.estados_civiles = response.data.estados_civiles;
                this.generos = response.data.generos;
                this.paises = response.data.paises;
                this.csrf_token = response.data.csrf_token;
                console.log(this.csrf_token);
            } catch (error) {
                this.errors = error.response.data;
            } finally {
                this.loading = false;
            }
        },
        resetFormulario() {
            this.formData = {
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
                },
                archivo: {
                    certificado_b1: null,
                    plan_trabajo: null,
                    carta_recomendacion: "",
                },
            }
        }  
    },

});