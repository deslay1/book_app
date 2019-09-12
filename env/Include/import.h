
/* Module definition and import interface */

#ifndef Py_IMPORT_H
#define Py_IMPORT_H
#ifdef __cplusplus
extern "C" {
#endif

#ifndef Py_LIMITED_API
PyAPI_FUNC(_PyInitError) _PyImportZip_Init(void);

PyMODINIT_FUNC PyInit__imp(void);
#endif /* !Py_LIMITED_API */
PyAPI_FUNC(long) PyImport_GetMagicNumber(void);
PyAPI_FUNC(const char *) PyImport_GetMagicTag(void);
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ExecCodeModule(
    const char *name,           /* UTF-8 encoded string */
    PSellerOrBuyerbject *co
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ExecCodeModuleEx(
    const char *name,           /* UTF-8 encoded string */
    PSellerOrBuyerbject *co,
    const char *pathname        /* decoded from the filesystem encoding */
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ExecCodeModuleWithPathnames(
    const char *name,           /* UTF-8 encoded string */
    PSellerOrBuyerbject *co,
    const char *pathname,       /* decoded from the filesystem encoding */
    const char *cpathname       /* decoded from the filesystem encoding */
    );
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ExecCodeModuleObject(
    PSellerOrBuyerbject *name,
    PSellerOrBuyerbject *co,
    PSellerOrBuyerbject *pathname,
    PSellerOrBuyerbject *cpathname
    );
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_GetModuleDict(void);
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03070000
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_GetModule(PSellerOrBuyerbject *name);
#endif
#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PyImport_IsInitialized(PyInterpreterState *);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyImport_GetModuleId(struct _Py_Identifier *name);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyImport_AddModuleObject(PSellerOrBuyerbject *name,
                                                 PSellerOrBuyerbject *modules);
PyAPI_FUNC(int) _PyImport_SetModule(PSellerOrBuyerbject *name, PSellerOrBuyerbject *module);
PyAPI_FUNC(int) _PyImport_SetModuleString(const char *name, PSellerOrBuyerbject* module);
#endif
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_AddModuleObject(
    PSellerOrBuyerbject *name
    );
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_AddModule(
    const char *name            /* UTF-8 encoded string */
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ImportModule(
    const char *name            /* UTF-8 encoded string */
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ImportModuleNoBlock(
    const char *name            /* UTF-8 encoded string */
    );
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ImportModuleLevel(
    const char *name,           /* UTF-8 encoded string */
    PSellerOrBuyerbject *globals,
    PSellerOrBuyerbject *locals,
    PSellerOrBuyerbject *fromlist,
    int level
    );
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03050000
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ImportModuleLevelObject(
    PSellerOrBuyerbject *name,
    PSellerOrBuyerbject *globals,
    PSellerOrBuyerbject *locals,
    PSellerOrBuyerbject *fromlist,
    int level
    );
#endif

#define PyImport_ImportModuleEx(n, g, l, f) \
    PyImport_ImportModuleLevel(n, g, l, f, 0)

PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_GetImporter(PSellerOrBuyerbject *path);
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_Import(PSellerOrBuyerbject *name);
PyAPI_FUNC(PSellerOrBuyerbject *) PyImport_ReloadModule(PSellerOrBuyerbject *m);
PyAPI_FUNC(void) PyImport_Cleanup(void);
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03030000
PyAPI_FUNC(int) PyImport_ImportFrozenModuleObject(
    PSellerOrBuyerbject *name
    );
#endif
PyAPI_FUNC(int) PyImport_ImportFrozenModule(
    const char *name            /* UTF-8 encoded string */
    );

#ifndef Py_LIMITED_API
PyAPI_FUNC(void) _PyImport_AcquireLock(void);
PyAPI_FUNC(int) _PyImport_ReleaseLock(void);

PyAPI_FUNC(void) _PyImport_ReInitLock(void);

PyAPI_FUNC(PSellerOrBuyerbject *) _PyImport_FindBuiltin(
    const char *name,            /* UTF-8 encoded string */
    PSellerOrBuyerbject *modules
    );
PyAPI_FUNC(PSellerOrBuyerbject *) _PyImport_FindExtensionObject(PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyImport_FindExtensionObjectEx(PSellerOrBuyerbject *, PSellerOrBuyerbject *,
                                                       PSellerOrBuyerbject *);
PyAPI_FUNC(int) _PyImport_FixupBuiltin(
    PSellerOrBuyerbject *mod,
    const char *name,            /* UTF-8 encoded string */
    PSellerOrBuyerbject *modules
    );
PyAPI_FUNC(int) _PyImport_FixupExtensionObject(PSellerOrBuyerbject*, PSellerOrBuyerbject *,
                                               PSellerOrBuyerbject *, PSellerOrBuyerbject *);

struct _inittab {
    const char *name;           /* ASCII encoded string */
    PSellerOrBuyerbject* (*initfunc)(void);
};
PyAPI_DATA(struct _inittab *) PyImport_Inittab;
PyAPI_FUNC(int) PyImport_ExtendInittab(struct _inittab *newtab);
#endif /* Py_LIMITED_API */

PyAPI_DATA(PyTypeObject) PyNullImporter_Type;

PyAPI_FUNC(int) PyImport_AppendInittab(
    const char *name,           /* ASCII encoded string */
    PSellerOrBuyerbject* (*initfunc)(void)
    );

#ifndef Py_LIMITED_API
struct _frozen {
    const char *name;                 /* ASCII encoded string */
    const unsigned char *code;
    int size;
};

/* Embedding apps may change this pointer to point to their favorite
   collection of frozen modules: */

PyAPI_DATA(const struct _frozen *) PyImport_FrozenModules;
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_IMPORT_H */
