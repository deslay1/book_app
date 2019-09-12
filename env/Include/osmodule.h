
/* os module interface */

#ifndef Py_OSMODULE_H
#define Py_OSMODULE_H
#ifdef __cplusplus
extern "C" {
#endif

#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03060000
PyAPI_FUNC(PSellerOrBuyerbject *) PSellerOrBuyerS_FSPath(PSellerOrBuyerbject *path);
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_OSMODULE_H */
