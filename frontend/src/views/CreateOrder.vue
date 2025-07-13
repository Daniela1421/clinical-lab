<template>
  <div class="container-fluid card card-body">
    <h4 class="mb-4">Crear Orden de Exámenes</h4>

    <form @submit.prevent="crearOrden">
      <div class="form-group">
        <label>Documento del paciente:</label>
        <input v-model="documento" type="text" class="form-control" required />
        <button class="btn btn-primary btn-md mt-2" @click.prevent="buscarPaciente">Buscar</button>
      </div>

      <div v-if="mensaje" :style="{ color: mensajeColor }" class="mt-3">
        {{ mensaje }}
      </div>

      <div v-if="paciente" class="mt-4">
        <p><strong>Paciente:</strong> {{ paciente.nombre_completo }}</p>

        <div class="form-group">
          <label>Seleccionar exámenes:</label>
          <div
            v-for="examen in examenes"
            :key="examen.id"
            class="form-check"
          >
            <input
              type="checkbox"
              class="form-check-input"
              :value="examen.id"
              v-model="examenesSeleccionados"
              :id="`examen-${examen.id}`"
            />
            <label :for="`examen-${examen.id}`" class="form-check-label">
              {{ examen.nombre }} ({{ examen.area }})
            </label>
          </div>
        </div>

        <button type="submit" class="btn btn-primary mt-3">Crear Orden</button>
      </div>
    </form>
  </div>
</template>

<script>
import api from "@/api";

export default {
  data() {
    return {
      documento: "",
      paciente: null,
      examenes: [],
      examenesSeleccionados: [],
      mensaje: "",
      mensajeColor: "green",
    };
  },
  methods: {
    async buscarPaciente() {
      this.mensaje = "";
      this.paciente = null;
      this.examenesSeleccionados = [];

      try {
        const res = await api.get(`/pacientes/documento/${this.documento}`);
        this.paciente = res.data;

        const examRes = await api.get("/examenes/");
        this.examenes = examRes.data;
      } catch (error) {
        this.mensaje = "Paciente no encontrado.";
        this.mensajeColor = "red";
      }
    },
    async crearOrden() {
      if (!this.examenesSeleccionados.length) {
        this.mensaje = "Selecciona al menos un examen.";
        this.mensajeColor = "red";
        return;
      }

      try {
        const ordenRes = await api.post("/ordenes/", {
          numero_orden: `ORD-${Math.floor(Math.random() * 10000)}`,
          id_paciente: this.paciente.id,
        });

        const ordenId = ordenRes.data.id;

        for (const examenId of this.examenesSeleccionados) {
          await api.post("/ordenes-examenes/", {
            id_orden: ordenId,
            id_examen: examenId,
          });
        }

        this.mensaje = "Orden creada correctamente.";
        this.mensajeColor = "green";
        this.resetFormulario();
      } catch (error) {
        this.mensaje = "Error al crear la orden.";
        this.mensajeColor = "red";
      }
    },
    resetFormulario() {
      this.documento = "";
      this.paciente = null;
      this.examenes = [];
      this.examenesSeleccionados = [];
    },
  },
};
</script>

<style scoped>
.container {
  margin: auto;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fdfdfd;
}
</style>

