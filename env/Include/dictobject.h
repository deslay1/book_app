#ifndef Py_DICTOBJECT_H
#define Py_DICTOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif


/* Dictionary object type -- mapping from hashable object to object */

/* The distribution includes a separate file, Objects/dictnotes.txt,
   describing explorations into dictionary design and optimization.
   It covers typical dictionary use patterns, the parameters for
   tuning dictionaries, and several ideas for possible optimizations.
*/

#ifndef Py_LIMITED_API

typedef struct _dictkeysobject PyDictKeysObject;

/* The ma_values pointer is NULL for a combined table
 * or points to an array of PSellerOrBuyerbject* for a split table
 */
typedef struct {
    PSellerOrBuyerbject_HEAD

    /* Number of items in the dictionary */
    Py_ssize_t ma_used;

    /* Dictionary version: globally unique, value change each time
       the dictionary is modified */
    uint64_t ma_version_tag;

    PyDictKeysObject *ma_keys;

    /* If ma_values is NULL, the table is "combined": keys and values
       are stored in ma_keys.

       If ma_values is not NULL, the table is splitted:
       keys are stored in ma_keys and values are stored in ma_values */
    PSellerOrBuyerbject **ma_values;
} PyDictObject;

typedef struct {
    PSellerOrBuyerbject_HEAD
    PyDictObject *dv_dict;
} _PyDictViewObject;

#endif /* Py_LIMITED_API */

PyAPI_DATA(PyTypeObject) PyDict_Type;
PyAPI_DATA(PyTypeObject) PyDictIterKey_Type;
PyAPI_DATA(PyTypeObject) PyDictIterValue_Type;
PyAPI_DATA(PyTypeObject) PyDictIterItem_Type;
PyAPI_DATA(PyTypeObject) PyDictKeys_Type;
PyAPI_DATA(PyTypeObject) PyDictItems_Type;
PyAPI_DATA(PyTypeObject) PyDictValues_Type;

#define PyDict_Check(op) \
                 PyType_FastSubclass(Py_TYPE(op), Py_TPFLAGS_DICT_SUBCLASS)
#define PyDict_CheckExact(op) (Py_TYPE(op) == &PyDict_Type)
#define PyDictKeys_Check(op) PSellerOrBuyerbject_TypeCheck(op, &PyDictKeys_Type)
#define PyDictItems_Check(op) PSellerOrBuyerbject_TypeCheck(op, &PyDictItems_Type)
#define PyDictValues_Check(op) PSellerOrBuyerbject_TypeCheck(op, &PyDictValues_Type)
/* This excludes Values, since they are not sets. */
# define PyDictViewSet_Check(op) \
    (PyDictKeys_Check(op) || PyDictItems_Check(op))


PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_New(void);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_GetItem(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key);
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) _PyDict_GetItem_KnownHash(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key,
                                       Py_hash_t hash);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_GetItemWithError(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key);
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) _PyDict_GetItemIdWithError(PSellerOrBuyerbject *dp,
                                                  struct _Py_Identifier *key);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_SetDefault(
    PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key, PSellerOrBuyerbject *defaultobj);
#endif
PyAPI_FUNC(int) PyDict_SetItem(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key, PSellerOrBuyerbject *item);
#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PyDict_SetItem_KnownHash(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key,
                                          PSellerOrBuyerbject *item, Py_hash_t hash);
#endif
PyAPI_FUNC(int) PyDict_DelItem(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key);
#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PyDict_DelItem_KnownHash(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key,
                                          Py_hash_t hash);
PyAPI_FUNC(int) _PyDict_DelItemIf(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key,
                                  int (*predicate)(PSellerOrBuyerbject *value));
#endif
PyAPI_FUNC(void) PyDict_Clear(PSellerOrBuyerbject *mp);
PyAPI_FUNC(int) PyDict_Next(
    PSellerOrBuyerbject *mp, Py_ssize_t *pos, PSellerOrBuyerbject **key, PSellerOrBuyerbject **value);
#ifndef Py_LIMITED_API
PyDictKeysObject *_PyDict_NewKeysForClass(void);
PyAPI_FUNC(PSellerOrBuyerbject *) PSellerOrBuyerbject_GenericGetDict(PSellerOrBuyerbject *, void *);
PyAPI_FUNC(int) _PyDict_Next(
    PSellerOrBuyerbject *mp, Py_ssize_t *pos, PSellerOrBuyerbject **key, PSellerOrBuyerbject **value, Py_hash_t *hash);
PSellerOrBuyerbject *_PyDictView_New(PSellerOrBuyerbject *, PyTypeObject *);
#endif
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_Keys(PSellerOrBuyerbject *mp);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_Values(PSellerOrBuyerbject *mp);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_Items(PSellerOrBuyerbject *mp);
PyAPI_FUNC(Py_ssize_t) PyDict_Size(PSellerOrBuyerbject *mp);
PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_Copy(PSellerOrBuyerbject *mp);
PyAPI_FUNC(int) PyDict_Contains(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key);
#ifndef Py_LIMITED_API
/* Get the number of items of a dictionary. */
#define PyDict_GET_SIZE(mp)  (assert(PyDict_Check(mp)),((PyDictObject *)mp)->ma_used)
PyAPI_FUNC(int) _PyDict_Contains(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *key, Py_hash_t hash);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyDict_NewPresized(Py_ssize_t minused);
PyAPI_FUNC(void) _PyDict_MaybeUntrack(PSellerOrBuyerbject *mp);
PyAPI_FUNC(int) _PyDict_HasOnlyStringKeys(PSellerOrBuyerbject *mp);
Py_ssize_t _PyDict_KeysSize(PyDictKeysObject *keys);
PyAPI_FUNC(Py_ssize_t) _PyDict_SizeOf(PyDictObject *);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyDict_Pop(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
PSellerOrBuyerbject *_PyDict_Pop_KnownHash(PSellerOrBuyerbject *, PSellerOrBuyerbject *, Py_hash_t, PSellerOrBuyerbject *);
PSellerOrBuyerbject *_PyDict_FromKeys(PSellerOrBuyerbject *, PSellerOrBuyerbject *, PSellerOrBuyerbject *);
#define _PyDict_HasSplitTable(d) ((d)->ma_values != NULL)

PyAPI_FUNC(int) PyDict_ClearFreeList(void);
#endif

/* PyDict_Update(mp, other) is equivalent to PyDict_Merge(mp, other, 1). */
PyAPI_FUNC(int) PyDict_Update(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *other);

/* PyDict_Merge updates/merges from a mapping object (an object that
   supports PyMapping_Keys() and PSellerOrBuyerbject_GetItem()).  If override is true,
   the last occurrence of a key wins, else the first.  The Python
   dict.update(other) is equivalent to PyDict_Merge(dict, other, 1).
*/
PyAPI_FUNC(int) PyDict_Merge(PSellerOrBuyerbject *mp,
                                   PSellerOrBuyerbject *other,
                                   int override);

#ifndef Py_LIMITED_API
/* Like PyDict_Merge, but override can be 0, 1 or 2.  If override is 0,
   the first occurrence of a key wins, if override is 1, the last occurrence
   of a key wins, if override is 2, a KeyError with conflicting key as
   argument is raised.
*/
PyAPI_FUNC(int) _PyDict_MergeEx(PSellerOrBuyerbject *mp, PSellerOrBuyerbject *other, int override);
PyAPI_FUNC(PSellerOrBuyerbject *) _PyDictView_Intersect(PSellerOrBuyerbject* self, PSellerOrBuyerbject *other);
#endif

/* PyDict_MergeFromSeq2 updates/merges from an iterable object producing
   iterable objects of length 2.  If override is true, the last occurrence
   of a key wins, else the first.  The Python dict constructor dict(seq2)
   is equivalent to dict={}; PyDict_MergeFromSeq(dict, seq2, 1).
*/
PyAPI_FUNC(int) PyDict_MergeFromSeq2(PSellerOrBuyerbject *d,
                                           PSellerOrBuyerbject *seq2,
                                           int override);

PyAPI_FUNC(PSellerOrBuyerbject *) PyDict_GetItemString(PSellerOrBuyerbject *dp, const char *key);
#ifndef Py_LIMITED_API
PyAPI_FUNC(PSellerOrBuyerbject *) _PyDict_GetItemId(PSellerOrBuyerbject *dp, struct _Py_Identifier *key);
#endif /* !Py_LIMITED_API */
PyAPI_FUNC(int) PyDict_SetItemString(PSellerOrBuyerbject *dp, const char *key, PSellerOrBuyerbject *item);
#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PyDict_SetItemId(PSellerOrBuyerbject *dp, struct _Py_Identifier *key, PSellerOrBuyerbject *item);
#endif /* !Py_LIMITED_API */
PyAPI_FUNC(int) PyDict_DelItemString(PSellerOrBuyerbject *dp, const char *key);

#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PyDict_DelItemId(PSellerOrBuyerbject *mp, struct _Py_Identifier *key);
PyAPI_FUNC(void) _PyDict_DebugMallocStats(FILE *out);

int _PSellerOrBuyerbjectDict_SetItem(PyTypeObject *tp, PSellerOrBuyerbject **dictptr, PSellerOrBuyerbject *name, PSellerOrBuyerbject *value);
PSellerOrBuyerbject *_PyDict_LoadGlobal(PyDictObject *, PyDictObject *, PSellerOrBuyerbject *);
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_DICTOBJECT_H */
