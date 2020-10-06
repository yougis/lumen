# Transforms

A [Transform](lumen.transforms.Transform) provides the ability to
transform the metric data supplied by a
[Source](lumen.sources.Source). Given a pandas `DataFrame` it applies
some transformation and returns another `DataFrame`.

```{eval-rst}
.. autoclass:: lumen.transforms.Transform
   :members:
```

## Transform types

```{eval-rst}
.. autoclass:: lumen.transforms.HistoryTransform
```