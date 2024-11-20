<template>
  <div>
    <!-- Primera Sección: Imagen a la derecha, Título y texto a la izquierda -->
    <section class="flex flex-col md:flex-row items-center py-16 px-4">
      <!-- Apartado de texto a la izquierda -->
      <div class="md:w-1/2 mb-8 md:mb-0 text-center md:text-left">
        <!-- Título con color personalizado -->
        <h2 class="text-5xl font-bold mb-3" style="color: #25535e">
          Relaciones Internacionales
        </h2>
        <p class="text-lg text-gray-600 dark:text-gray-600">
          La Universidad Nacional de La Plata constituye uno de los centros más
          prestigiosos del sistema de investigación y docencia nacional, lo que
          la convierte en punto de referencia obligada en la formación del
          acervo cultural universitario de nuestro país. <br>
          La <strong style="color: #25535e">Prosecretaría de Relaciones Internacionales (PRI)</strong>, busca trabajar estrategias de fortalecimiento e
          integración junto a la articulación entre instituciones y recursos, lo que implica garantizar una cooperación
          internacional compartida y permanente.
        </p>
      </div>
      <!-- Imagen a la derecha -->
      <div class="md:w-1/2">
        <img src="../assets/estudiantes-landing-page.jpg" alt="Imagen descriptiva"
          class="w-full h-auto object-cover rounded-lg shadow-lg" />
      </div>
    </section>

    <!-- Segunda Sección: Carrusel de Cards con Flowbite -->
    <section class="py-16 px-4" style="background-color: #96ba3a">
      <h3 class="text-5xl mb-4 font-bold text-center text-white">
        Nuestras Facultades
      </h3>
      <div class="container mx-auto py-8">
        <CardCarousel :cards="cards" />
      </div>
    </section>
  </div>
</template>

<script>
import CardCarousel from '../components/CardCarousel.vue';
import fau_image from '../assets/logo-fau.png';
import artes_image from '../assets/logo-arte.jpg';
import agraria_image from '../assets/logo-agraria.png';
import astronomica_image from '../assets/logo-astronomica.png';
import economicas_image from '../assets/logo-economicas.png';
import exactas_image from '../assets/logo-exactas.jpg';
import juridicas_image from '../assets/logo-juridica.jpg';
import medicina_image from '../assets/logo-medicina.png';
import naturales_image from '../assets/logo-naturales.png';
import veterinaria_image from '../assets/logo-veterinaria.png';
import humanidades_image from '../assets/logo-humanidades.png';
import informatica_image from '../assets/logo-informatica.png';
import ingenieria_image from '../assets/logo-ingenieria.png';
import odontologia_image from '../assets/logo-odontologia.png';
import periodismo_image from '../assets/logo-periodismo.png';
import psicologia_image from '../assets/logo-psicologia.png';
import social_image from '../assets/logo-trabajo-social.jpg';

export default {
  components: {
    CardCarousel
  },
  data() {
    return {
      cards: [
        {
          title: 'Facultad de Arquitectura y Urbanismo',
          description: 'Calle 47 y 117 nº 162 – La Plata (C.P. 1900)',
          contactPhone: '(0221)423-6587/90',
          contactEmail: 'decanato@fau.unlp.edu.ar',
          link: 'https://www.fau.unlp.edu.ar/?_gl=1*1q15hlh*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: fau_image
        },
        {
          title: 'Facultad de Artes',
          description: 'Diag. 78 nro.680 – La Plata (C.P.1900)',
          contactPhone: '(0221) 423-6598 // 423-5756',
          contactEmail: 'academica@fba.unlp.edu.ar',
          link: 'https://fba.unlp.edu.ar/?_gl=1%2Ah4p48c%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: artes_image
        },
        {
          title: 'Facultad de Ciencias Agrarias y Forestales',
          description: 'Avda. 60 y 119 -S/Nº- La Plata (C.P. 1900)',
          contactPhone: '(0221) 423-6758',
          contactEmail: 'decano@agro.unlp.edu.ar',
          link: 'https://www.agro.unlp.edu.ar/?_gl=1*1fupplp*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: agraria_image
        },
        {
          title: 'Facultad de Ciencias Astronómicas y Geofísicas',
          description: 'Paseo del Bosque s/n La Plata (C.P.1900)',
          contactPhone: '(0221) 4236593/4236759/4236594/4236592',
          contactEmail: 'extension@fcaglp.unlp.edu.ar',
          link: 'https://www.fcaglp.unlp.edu.ar/?_gl=1%2Aqha31o%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: astronomica_image
        },
        {
          title: 'Facultad de Ciencias Económicas',
          description: 'Calle 6 entre 47 y 48 La Plata (C.P. 1900)',
          contactPhone: '(0221) 423-6769/71/72',
          contactEmail: 'decanato@econo.unlp.edu.ar',
          link: 'https://www.econo.unlp.edu.ar/?_gl=1*var5zz*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: economicas_image
        },
        {
          title: 'Facultad de Ciencias Exactas',
          description: 'Calle 47 y 115 La Plata (C.P. 1900)',
          contactPhone: '(0221) 422-6977/6979/6981',
          contactEmail: 'academic@decanato.exactas.unlp.edu.ar',
          link: 'https://www.exactas.unlp.edu.ar/?_gl=1*5tezet*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: exactas_image
        },
        {
          title: 'Facultad de Ciencias Jurídicas y Sociales',
          description: 'Calle 48 entre 6y7 La Plata (C.P.1900)',
          contactPhone: '(221) 644-2070/644-2090',
          contactEmail: 'decanato@jursoc.unlp.edu.ar',
          link: 'https://www.jursoc.unlp.edu.ar/?_gl=1*rri028*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: juridicas_image
        },
        {
          title: 'Facultad de Ciencias Médicas',
          description: 'Calle 60 y 120 La Plata (C.P. 1900)',
          contactPhone: '(0221) 424-1596/424-3068/424-2711/423-6711',
          contactEmail: 'alumnado@med.unlp.edu.ar',
          link: 'https://www.med.unlp.edu.ar/?_gl=1*rri028*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjEzOTE0Ni4xMy4wLjE3MzIxMzkxNDcuMC4wLjA.',
          image: medicina_image
        },
        {
          title: 'Facultad de Ciencias Naturales y Museo',
          description: 'Calle 60 y 122 La Plata (C.P. 1900)',
          contactPhone: '(0221) 423-6773/ 425-8252/ 423-2734',
          contactEmail: 'fcnym@museo.fcnym.unlp.edu.ar',
          link: 'https://www.fcnym.unlp.edu.ar/?_gl=1%2A1mq7hjc%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: naturales_image
        },
        {
          title: 'Facultad de Ciencias Veterinarias',
          description: 'Calle 60 y 118 La Plata (C.P. 1900)',
          contactPhone: '(0221) 423-6663/ 423-6664/ 424-7642',
          contactEmail: 'prensaydifusion@fcv.unlp.edu.ar',
          link: 'https://www.fcv.unlp.edu.ar/?_gl=1%2A7qa7ng%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: veterinaria_image
        },
        {
          title: 'Facultad de Humanidades y Ciencias de la Educación',
          description: 'Calle 51 e/124 y 125 Ensenada',
          contactPhone: '4230128/4236669/4230125/4236673',
          contactEmail: 'sae@fahce.unlp.edu.ar',
          link: 'https://www.fahce.unlp.edu.ar/?_gl=1*1xxjz3v*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: humanidades_image
        },
        {
          title: 'Facultad de Informática',
          description: 'Calle 50 y 120 La Plata (C.P.1900)',
          contactPhone: '(0221) 4277270',
          contactEmail: 'difusion@info.unlp.edu.ar',
          link: 'https://www.info.unlp.edu.ar/?_gl=1%2A16864dd%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: informatica_image
        },
        {
          title: 'Facultad de Ingeniería',
          description: 'Calle 1 y 47 La Plata (C.P. 1900)',
          contactPhone: '(0221) 425-8911/ 423-6676',
          contactEmail: 'secretaria.academica@ing.unlp.edu.ar',
          link: 'https://ing.unlp.edu.ar/?_gl=1%2Aekd3v3%2A_ga%2AMTI5MjM3OTgyMy4xNzEwNDQ5MTU3%2A_ga_JSX0RPJKK5%2AMTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: ingenieria_image
        },
        {
          title: 'Facultad de Odontología',
          description: 'Calle 1 y 50 La Plata (C.P.1900)',
          contactPhone: '(0221) 423-6775',
          contactEmail: 'decanato@folp.unlp.edu.ar',
          link: 'https://www.folp.unlp.edu.ar/?_gl=1*m9rrpx*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: odontologia_image
        },
        {
          title: 'Facultad de Periodismo y Comunicación Social',
          description: 'Diagonal 113 y 63 - Calle 44 nº 676 entre 8 y 9',
          contactPhone: '(0221) 4250133 (Sede Diagonal) - (0221) 423-6778/83/84 (Sede 44)',
          contactEmail: 'decanato@perio.unlp.edu.ar',
          link: 'https://perio.unlp.edu.ar/',
          image: periodismo_image
        },
        {
          title: 'Facultad de Psicología',
          description: 'Calle 51 entre 122 y 123',
          contactPhone: '482-4415/482-5931/482-8457',
          contactEmail: 'decanato@psico.unlp.edu.ar',
          link: 'https://www.psico.unlp.edu.ar/?_gl=1*j18lp6*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: psicologia_image
        },
        {
          title: 'Facultad de Trabajo Social',
          description: 'Calle 9 esq. 63 La Plata (C.P.1900)',
          contactPhone: '(0221)452-5317',
          contactEmail: 'comunicacioninstitucional@trabajosocial.unlp.edu.ar',
          link: 'https://www.trabajosocial.unlp.edu.ar/?_gl=1*1m918fy*_ga*MTI5MjM3OTgyMy4xNzEwNDQ5MTU3*_ga_JSX0RPJKK5*MTczMjE0MjM4Mi4xNC4wLjE3MzIxNDIzODkuMC4wLjA.',
          image: social_image
        }
      ]
    };
  }
};
</script>
