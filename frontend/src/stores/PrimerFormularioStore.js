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
        },
        errors: null,
        loading: false,
        paises: [],
        generos: [],
        estados_civiles: [],
        convenioPrograma: "",
        nivelEstudio: "",
        es_hispanohablante: false,
        mercosur: false,
        csrf_token: "",
    }),
    actions: {
        async submitForm() {
            this.loading = true;
            try {
                console.log("este es el form data:");
                console.log("holaaaaaa");
                

                // Convertir archivos a Base64
                const archivos = this.formData.archivo;

                for (const key in archivos) {
                    if (archivos[key]) {
                        archivos[key] = await this.convertToBase64(archivos[key]);
                    }
                }
                console.log(this.formData);
                console.log("así estan los archivos");
                console.log(this.formData.archivo);
                //axios.defaults.headers.post['X-CSRF-Token'] = this.csrf_token;
                const response = await axios.post('http://127.0.0.1:5000/api/postulacion/primer-formulario', this.formData, 
                    {
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRF-Token': this.csrf_token,
                        },
                    },
                ).then(response => {
                    console.log(response);
                });
                this.errors = null;
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
                const response = await axios.get('http://127.0.0.1:5000/api/postulacion/primer-formulario-data',
                );
                this.errors = null;
                this.estados_civiles = response.data.estados_civiles;
                this.generos = response.data.generos;
                this.paises = response.data.paises;
                this.csrf_token = response.data.csrf_token;
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
        }
            
    },

});