# VDM-RT Orthad Listen-Only Probe

**The harness never scans, never reduces the graph, never asks the engine a question. It only receives what the walkers announce and passes it through.**

This package starts from the supplied VDM-RT engine and adds a structured Orthad state input source plus a listen-only runner. The decoder/language path is not used. The original engine, connectome, scouts, maps, ADC, B1, event adapter, and runtime dynamics are left intact.

## Run

```bash
python -m vdm_rt.run_orthad_listen \
  --N 500 --walkers 600 --ticks 48 --seeds 0,1,2 \
  --out-dir outputs --run-root runs/orthad_listen_probe
```

The local smoke uses the same occupancy ratio as the best Aura-scale run:

```text
5000 neurons : 6000 walkers = 1.2 walkers/neuron
500 neurons  : 600 walkers  = 1.2 walkers/neuron
```

## Outputs

- `outputs/result_card.json`
- `outputs/scenario_summary.csv`
- `outputs/tick_listen_rows.csv`

## Firewall

The probe installs a scan firewall over the common graph-read methods:

```text
active_edge_count
connected_components
cyclomatic_complexity
connectome_entropy
snapshot_graph
```

If the harness calls one of these, the run fails.
