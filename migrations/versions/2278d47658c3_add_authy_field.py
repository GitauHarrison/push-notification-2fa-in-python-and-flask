"""add authy field

Revision ID: 2278d47658c3
Revises: 05573d400d7b
Create Date: 2021-03-26 05:39:01.478725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2278d47658c3'
down_revision = '05573d400d7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('authy_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_user_authy_id'), 'user', ['authy_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_authy_id'), table_name='user')
    op.drop_column('user', 'authy_id')
    # ### end Alembic commands ###