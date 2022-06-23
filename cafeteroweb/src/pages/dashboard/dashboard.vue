<template>
    <!-- Content Header (Page header) -->
    <div class="content-header">
        <div class="container-fluid">
            <div class="row mb-2">
                <div class="col-sm-6">
                    <h1 class="m-0">Estadísticas</h1>
                </div>
                <!-- /.col -->

                <!-- /.col -->
            </div>
            <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
    </div>
    <!-- /.content-header -->

    <!-- Main content -->
    <section class="content">
        <div class="container-fluid">
            <!-- Small boxes (Stat box) -->
            <div class="row">
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-primary">
                        <div class="inner">
                            <h3>{{ counts.recoleccion }} Lotes</h3>

                            <p>Recolección</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-bag"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-primary">
                        <div class="inner">
                            <h3>{{ counts.despulpado }} Lotes</h3>

                            <p>Despulpado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-stats-bars"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-secondary">
                        <div class="inner">
                            <h3>{{ counts.fermentacion }} Lotes</h3>

                            <p>Fermentación</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-person-add"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-secondary">
                        <div class="inner">
                            <h3>{{ counts.lavado }} Lotes</h3>

                            <p>Lavado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-pie-graph"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
            </div>
            <!-- /.row -->
            <!-- Small boxes (Stat box) -->
            <div class="row">
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-success">
                        <div class="inner">
                            <h3>{{ counts.secado }} Lotes</h3>

                            <p>Secado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-bag"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-success">
                        <div class="inner">
                            <h3>{{ counts.trillado }} Lotes</h3>

                            <p>Trillado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-stats-bars"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-info">
                        <div class="inner">
                            <h3>{{ counts.almacenado }} Lotes</h3>

                            <p>Almacenado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-person-add"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-danger">
                        <div class="inner">
                            <h3>{{ counts.tostado }} Lotes</h3>

                            <p>Tostado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-pie-graph"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
                <!-- ./col -->
            </div>
            <!-- /.row -->
            <!-- Small boxes (Stat box) -->
            <div class="row">
                <div class="col-lg-3 col-6">
                    <!-- small box -->
                    <div class="small-box bg-warning">
                        <div class="inner">
                            <h3>{{ counts.etiquetado }} Lotes</h3>

                            <p>Etiquetado</p>
                        </div>
                        <div class="icon">
                            <i class="ion ion-bag"></i>
                        </div>
                        <router-link to="/batch" class="small-box-footer"
                            >Más información
                            <i class="fas fa-arrow-circle-right"></i
                        ></router-link>
                    </div>
                </div>
            </div>
            <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
    </section>
    <!-- /.content -->
</template>
<script lang="ts">
import {defineComponent} from 'vue';
import BatchDataService from '@/services/BatchDataService';
import Batch from '@/types/Batch';
import ResponseData from '@/types/ResponseData';
import {useToast} from 'vue-toastification';

let toast = useToast();
export default defineComponent({
    name: 'batchs-list',
    data() {
        return {
            batchs: [] as Batch[],
            currentBatch: {} as Batch,
            currentIndex: -1,
            update: false,
            list: true,
            title: '',
            counts: {
                recoleccion: null,
                despulpado: null,
                fermentacion: null,
                lavado: null,
                secado: null,
                trillado: null,
                almacenado: null,
                tostado: null,
                etiquetado: null
            }
        };
    },
    methods: {
        retrieveBatch() {
            BatchDataService.getAll()
                .then((response: ResponseData) => {
                    this.batchs = response.data;
                })
                .catch((e: Error) => {
                    console.log(e);
                });
        },
        refreshList() {
            this.retrieveBatch();
            this.currentBatch = {} as Batch;
            this.currentIndex = -1;
        },
        setActiveBatch(batch: Batch, index = -1) {
            this.currentBatch = batch;
            this.currentIndex = index;
            this.update = true;
            this.list = false;
        },
        setDesactiveBatch() {
            this.update = false;
            this.list = true;
        }
    },
    created() {
        this.counts.recoleccion = 0;
        this.counts.despulpado = 1;
        this.counts.fermentacion = 0;
        this.counts.lavado = 0;
        this.counts.secado = 0;
        this.counts.trillado = 0;
        this.counts.almacenado = 0;
        this.counts.tostado = 0;
        this.counts.etiquetado = 0;
    },
    mounted() {
        this.retrieveBatch();
    }
});
</script>
<style lang="scss"></style>