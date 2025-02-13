def discard(self, n=-1, qid=-1, dehydration_hooks=None,
            hydration_hooks=None, **handlers):
    if dehydration_hooks is None:
        dehydration_hooks = {}
    if hydration_hooks is None:
        hydration_hooks = {}

    message = {
        'type': 'DISCARD',
        'n': n,
        'qid': qid,
        'dehydration_hooks': dehydration_hooks,
        'hydration_hooks': hydration_hooks,
        'handlers': handlers
    }
    
    self.output_queue.append(message)