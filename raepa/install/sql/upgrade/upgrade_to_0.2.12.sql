BEGIN;

CREATE INDEX raepa_apparass_p_geom_idx1 ON raepa.raepa_apparass_p USING gist (geom);
CREATE INDEX raepa_canalaep_l_geom_idx1 ON raepa.raepa_canalaep_l USING gist (geom);
CREATE INDEX raepa_canalaep_l_st_endpoint_idx1 ON raepa.raepa_canalaep_l USING gist (public.st_endpoint(geom));
CREATE INDEX raepa_canalaep_l_st_startpoint_idx1 ON raepa.raepa_canalaep_l USING gist (public.st_startpoint(geom));
CREATE INDEX raepa_canalass_l_geom_idx1 ON raepa.raepa_canalass_l USING gist (geom);
CREATE INDEX raepa_ouvraep_p_geom_idx1 ON raepa.raepa_ouvraep_p USING gist (geom);
CREATE INDEX raepa_ouvrass_p_geom_idx1 ON raepa.raepa_ouvrass_p USING gist (geom);
CREATE INDEX raepa_reparaep_p_geom_idx1 ON raepa.raepa_reparaep_p USING gist (geom);
CREATE INDEX raepa_reparass_p_geom_idx1 ON raepa.raepa_reparass_p USING gist (geom);

COMMIT;
