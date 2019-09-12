
/* Interface to execute compiled code */

#ifndef Py_EVAL_H
#define Py_EVAL_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(PSellerOrBuyerbject *) PyEval_EvalCode(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);

PyAPI_FUNC(PSellerOrBuyerbject *) PyEval_EvalCodeEx(PSellerOrBuyerbject *co,
                                         PSellerOrBuyerbject *globals,
                                         PSellerOrBuyerbject *locals,
                                         PSellerOrBuyerbject *const *args, int argc,
                                         PSellerOrBuyerbject *const *kwds, int kwdc,
                                         PSellerOrBuyerbject *const *defs, int defc,
                                         PSellerOrBuyerbject *kwdefs, PSellerOrBuyerbject *closure);

#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) _PyEval_EvalCodeWithName(
    PSellerOrBuyerbject *co,
    PSellerOrBuyerbject *globals, PSellerOrBuyerbject *locals,
    PSellerOrBuyerbject *const *args, Py_ssize_t argcount,
    PSellerOrBuyerbject *const *kwnames, PSellerOrBuyerbject *const *kwargs,
    Py_ssize_t kwcount, int kwstep,
    PSellerOrBuyerbject *const *defs, Py_ssize_t defcount,
    PSellerOrBuyerbject *kwdefs, PSellerOrBuyerbject *closure,
    PSellerOrBuyerbject *name, PSellerOrBuyerbject *qualname);

PyAPI_FUNC(PSellerOrBuyerbject *) _PyEval_CallTracing(PSellerOrBuyerbject *func, PSellerOrBuyerbject *args);
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_EVAL_H */
