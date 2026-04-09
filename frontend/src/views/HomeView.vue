<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import * as echarts from 'echarts/core'
import { BarChart } from 'echarts/charts'
import { GridComponent, TitleComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import type { ECharts } from 'echarts/core'
import http from '@/api/http'

echarts.use([BarChart, GridComponent, TitleComponent, CanvasRenderer])

const apiHealth = ref<string>('-')
const dbHealth = ref<string>('-')
const chartRef = ref<HTMLDivElement | null>(null)
let chart: ECharts | null = null
let resizeObserver: ResizeObserver | null = null

async function checkApi() {
  try {
    const { data } = await http.get<{ status: string }>('/api/v1/health')
    apiHealth.value = data.status
    ElMessage.success(`API ${data.status}`)
  } catch {
    apiHealth.value = 'error'
    ElMessage.error('API 不可用')
  }
}

async function checkDb() {
  try {
    const { data } = await http.get<{ status: string; database?: boolean }>(
      '/api/v1/health/db',
    )
    dbHealth.value = data.database ? 'ok' : data.status
    ElMessage.success('数据库连接正常')
  } catch {
    dbHealth.value = 'error'
    ElMessage.error('数据库不可用（请配置 MySQL 与 DATABASE_URL）')
  }
}

onMounted(() => {
  const el = chartRef.value
  if (!el) return
  chart = echarts.init(el)
  chart.setOption({
    title: { text: '示例图表（ECharts）', left: 'center' },
    xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] },
    yAxis: { type: 'value' },
    series: [{ type: 'bar', data: [12, 20, 15, 8, 22] }],
    grid: { left: 48, right: 24, bottom: 32, top: 48 },
  })
  resizeObserver = new ResizeObserver(() => chart?.resize())
  resizeObserver.observe(el)
})

onUnmounted(() => {
  resizeObserver?.disconnect()
  resizeObserver = null
  chart?.dispose()
  chart = null
})
</script>

<template>
  <div class="home">
    <el-card shadow="never">
      <template #header>联调</template>
      <el-space wrap>
        <el-tag>API: {{ apiHealth }}</el-tag>
        <el-tag type="info">DB: {{ dbHealth }}</el-tag>
        <el-button type="primary" @click="checkApi">检查 API</el-button>
        <el-button @click="checkDb">检查数据库</el-button>
      </el-space>
      <p class="hint">
        开发环境可将 <code>VITE_API_BASE_URL</code> 留空，通过 Vite 代理访问
        <code>/api</code>。
      </p>
    </el-card>

    <el-card class="chart-card" shadow="never">
      <template #header>图表占位</template>
      <div ref="chartRef" class="chart" />
    </el-card>
  </div>
</template>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.hint {
  margin-top: 12px;
  color: var(--el-text-color-secondary);
  font-size: 13px;
}
.chart-card {
  width: 100%;
}
.chart {
  height: 280px;
  width: 100%;
}
</style>
